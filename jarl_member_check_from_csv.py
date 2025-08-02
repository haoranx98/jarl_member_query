import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def initialize_browser():
    """初始化浏览器实例"""
    # 设置 Firefox 驱动路径
    driver_path = "/home/haoranx98/Downloads/geckodriver-v0.36.0-linux64/geckodriver"  # 根据你存放 geckodriver 的路径调整

    # 初始化 Firefox 驱动服务
    service = Service(driver_path)

    # 初始化 WebDriver（这里用的是 Firefox）
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")  # 可选：无头模式，不弹出浏览器
    driver = webdriver.Firefox(service=service, options=options)

    return driver


def check_jarl_membership(driver, call_signs: str) -> str:
    """使用 Selenium 查询 JARL 会员状态"""

    # 访问 JARL 查询页面
    url = "https://www.jarl.com/Page/Search/MemberSearch.aspx?Language=En"
    driver.get(url)

    # 等待页面加载，直到输入框出现
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "txtCallSign")))

    # 查找输入框并输入多个呼号
    call_sign_input = driver.find_element(By.ID, "txtCallSign")
    call_sign_input.clear()
    call_sign_input.send_keys(call_signs)  # 这里输入多个呼号，空格分隔

    # 点击搜索按钮
    search_button = driver.find_element(By.ID, "btnSearch")
    search_button.click()

    # 等待结果加载
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@id='ListView2_lblCallSign_0']")))

    # 获取查询结果
    results = []
    for i in range(20):  # 假设最多可以查询 20 个呼号
        try:
            call_sign_result = driver.find_element(By.XPATH, f"//span[@id='ListView2_lblCallSign_{i}']").text.strip()
            result = driver.find_element(By.XPATH, f"//span[@id='ListView2_lblResult_{i}']").text.strip()
            results.append(f"{call_sign_result} 查询结果: {result}")
        except Exception as e:
            # 如果某个呼号查询不到结果，跳过
            continue

    return "\n".join(results)


def read_call_signs_from_csv(file_path: str):
    """读取 CSV 文件并返回呼号列表"""
    call_signs = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # 确保行不为空
                call_signs.append(row[0].strip())  # 获取每行的第一列（呼号）
    return call_signs


def write_results_to_file(results: str, output_file_path: str):
    """将结果写入文件"""
    with open(output_file_path, mode='w') as file:
        file.write(results)


if __name__ == "__main__":
    # 获取命令行输入的文件路径
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_callsign_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    # 确保输入文件存在
    if not os.path.isfile(input_file_path):
        print(f"Error: The file {input_file_path} does not exist.")
        sys.exit(1)

    # 获取文件所在目录
    directory = os.path.dirname(input_file_path)
    output_file_path = os.path.join(directory, "result.txt")

    # 初始化浏览器实例
    driver = initialize_browser()

    # 从 CSV 文件中读取呼号
    call_signs = read_call_signs_from_csv(input_file_path)

    # 每次最多查询 20 个呼号，拼接为一个字符串，以空格分隔
    batch_size = 20
    all_results = []
    for i in range(0, len(call_signs), batch_size):
        batch = " ".join(call_signs[i:i + batch_size])
        print(f"查询呼号: {batch}")
        result = check_jarl_membership(driver, batch)
        all_results.append(result)

    # 将所有查询结果写入 result.txt 文件
    write_results_to_file("\n".join(all_results), output_file_path)

    print(f"结果已保存到 {output_file_path}")

    # 在所有查询结束后关闭浏览器
    driver.quit()

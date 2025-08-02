
# JARL Membership Query (JARL 会员查询)

This project allows you to query JARL (Japan Amateur Radio League) membership information by calling signs. It automates the process using Selenium, querying the membership status from the JARL website.

本项目允许您通过呼号查询 JARL（日本业余无线电联盟）会员信息。该项目使用 Selenium 自动化查询过程，从 JARL 网站获取会员状态。

## Features 功能

- Query multiple calling signs in batch 查询多个呼号
- Save the result to a `result.txt` file 将查询结果保存到 `result.txt` 文件
- Support CSV input and output 支持 CSV 输入和输出

## Requirements 安装要求

- Python 3.x
- Selenium
- WebDriver (e.g., ChromeDriver, GeckoDriver)

### Install Dependencies 安装依赖

To install the required dependencies, you can use the following command:

```bash
conda env create -f environment.yml
```

要安装所需的依赖，可以使用以下命令：

```bash
conda env create -f environment.yml
```

### WebDriver 安装

You need to download a WebDriver that is compatible with the browser you are using (e.g., ChromeDriver for Chrome or GeckoDriver for Firefox).

- **ChromeDriver**: https://sites.google.com/a/chromium.org/chromedriver/
- **GeckoDriver**: https://github.com/mozilla/geckodriver/releases

### WebDriver 路径配置

Make sure to configure the correct WebDriver path in the `initialize_browser()` function.

确保在 `initialize_browser()` 函数中配置正确的 WebDriver 路径。

## Usage 使用方法

1. Clone this repository:

   克隆这个仓库：

   ```bash
   git clone https://github.com/your_username/jarl-membership-query.git
   cd jarl-membership-query
   ```

2. Prepare a CSV file (`callsign.csv`) with the calling signs you want to query. Each calling sign should be on a new line without any extra spaces.

   准备一个 CSV 文件（`callsign.csv`），文件中每行包含一个要查询的呼号。每个呼号应该单独一行，且不要包含额外空格。

3. Run the script, passing the path of your CSV file:

   运行脚本，传入您的 CSV 文件路径：

   ```bash
   python jarl_query.py /path/to/callsign.csv
   ```

4. The results will be saved in a `result.txt` file in the same directory where the script is located.

   查询结果将保存在与脚本相同目录下的 `result.txt` 文件中。

## Example 示例

### CSV File Example (`callsign.csv`)：

```
JG1YBO,
JL1BCR,
JK2XXK,
```

### Output Example (`result.txt`)：

```
7K4DHB 查询结果: ○ Yes
7L1WQO 查询结果: ○ Yes
7L3AEO 查询结果: ○ Yes
```

## Contributing 贡献

Feel free to open an issue or submit a pull request if you want to contribute to this project.

如果你想为这个项目做贡献，随时可以提出问题或提交拉取请求。

## License 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目使用 MIT 许可证 - 详细信息请参阅 [LICENSE](LICENSE) 文件。

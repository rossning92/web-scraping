这个仓库是 ep31 的源代码。

# 文件介绍

- hello_scraper.js - 使用 Puppeteer 爬取 bilibili 2020 年度翻唱区的热门视频。
- analysis.py - Python 脚本用于分析出现最频繁的词汇并生成词云图。

# 环境配置

- 若没有安装 Node.js 运行时，请下载安装：https://nodejs.org/
- 安装关联: `npm i`

# 运行爬虫脚本

- 使用 `node hello_scraper.js` 运行爬虫脚本
- 生成的数据将保存在 `data.json` 文件下

# 生成词云图

- 使用 `pip install jieba wordcloud pillow` 安装关联
- `python analysis.py`
- 生成的词云图将保存为 `word-cloud.png`

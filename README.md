﻿# 爬取疫情信息
爬取丁香园网站中，2020年1月27日到6月15日的感染情况，不仅包括国内各省份、个城市和总体感染情况，还包括全球各国的感染情况
以及每天疫情相关的新闻报道。
  爬取时可直接运行main.py，爬取数据的代码在service文件夹中。
# 数据整理与可视化
爬取的数据在DB数据库中，处理成csv文件后再进行整理。
  数据在src文件夹中，经过处理最后得到三个csv文件：全球感染情况、国内1-5月感染情况和国内各省份感染情况。
  打开covid-19.html，然后选择上面三个文件的其中一个，即可看到该文件的可视化。使用条状图排名，并动态显示。

# **Author**
Written by [camera](https://github.com/creama?tab=repositories)

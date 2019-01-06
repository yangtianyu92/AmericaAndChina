#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 10:58
# @Email    : yangtianyu92@126.com
import requests
import re
from bs4 import BeautifulSoup

url_dpac = "http://www.dpac.gov.cn/xfpzh/xfpgnzh/index{0}.html"


for i in range(47, 60):
    if i == 0:
        url_dpac1 = "http://www.dpac.gov.cn/xfpzh/xfpgnzh/index.html"
        response = requests.get(url_dpac1)
        response.encoding = "utf-8"
    else:
        response = requests.get(url_dpac.format('_'+str(i)))
        response.encoding = "utf-8"
    print("this is page: " + str(i))
    url_list = re.findall("<li><a href=\"\.(.*?)\"\stitle=", response.text)
    for url in url_list:
        url_raw = "http://www.dpac.gov.cn/xfpzh/xfpgnzh" + url
        response_raw = requests.get(url_raw)
        response_raw.encoding = "utf-8"
        s = BeautifulSoup(response_raw.text, "lxml")
        soup = s.h1.text
        soup2 = soup.replace('/', '').replace('*', '').replace('\“', '').replace('.', '').replace(':', '')
        with open("dpac/indoor/" + soup2 + ".html", "w", encoding="utf-8") as f:
            f.write(response_raw.text)
        print(soup2)


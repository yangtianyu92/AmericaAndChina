#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 22:02
# @Email    : yangtianyu92@126.com
import requests
import re
from bs4 import BeautifulSoup

url_cpsc = "https://www.cpsc.gov/Recalls"

url_base = "https://www.cpsc.gov"

response = requests.get(url=url_cpsc)

a = re.findall("<span class=\"field-content\"><a href=\"(.*?)\"", response.text)

for index, i in enumerate(range(139, 147)):
    url2 = url_cpsc + "?page=" + str(i)
    response1 = requests.get(url2)
    url_product = re.findall("<span class=\"field-content\"><a href=\"(.*?)\"", response1.text)
    url_product2 = [url_base+u for u in url_product]
    for urls in url_product2:
        response3 = requests.get(url=urls).text
        soup = BeautifulSoup(response3, "lxml")
        title = soup.title.text
        words = re.findall("\w+", title)
        titles = ''.join(words)
        print(titles)
        with open("cpsc/" + titles + ".html", "w", encoding="utf-8") as f:
            f.write(response3)
    print(index)






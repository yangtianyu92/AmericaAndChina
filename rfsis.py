#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 9:17
# @Email    : yangtianyu92@126.com
import requests
from bs4 import BeautifulSoup
import re


url_fsis = "https://www.usda.usda.gov/wps/portal/usda/topics/\
recalls-and-public-health-alerts/current-recalls-and-alerts/recalls-and-public-health-alerts"

base_url_fsis = "https://www.usda.usda.gov/wps/portal/usda/topics/recalls-and-public-health-alerts/\
current-recalls-and-alerts/recalls-and-public-health-alerts/\
!ut/p/a1/jZDBCoJAEIafpQdYdkwRPYpgaukikdleYjPThW2VVTv09Cl1yChy5jTD9_MxgynOMJXsxkvW8VoyMc7UPEICpma7EBLP8SCIdS\
-14pUGxByAwwSwtRFIE7J2XbBifWb-RznwLx_OECxV5EYlpg3rKsTlpcZZ3itVyA6pImdCtIjJM2KiUF2Ls_dd058Ez1FVMDFkX8Qe06kV\
tKEH69bww1gHYnwCX97yBH7f3Vx32X3jAw-cxQPrBMoV/"

base_url1 = "https://www.usda.usda.gov/wps/portal/usda/topics/recalls-and-public-health-alerts/current-recalls-and-alerts/recalls-and-public-health-alerts／"

base_url2 = "https://www.usda.usda.gov"

response = requests.get(url=url_fsis)

url_2017_2018 = re.findall("<li dir=\"ltr\"><a href=\"(.*?)\">", response.text)
url_2015_2016 = re.findall("<ul dir=\"ltr\">\\n\s<li><a href=\"(.*?)\">", response.text, re.M)


def iswps(url):
    return url[:4] == "/wps"


def iswhat(url):
    return url[0] == "?"


what1 = filter(iswhat, url_2015_2016)
what2 = filter(iswhat, url_2017_2018)
what_urls = list(what1) + list(what2)


for url in what_urls:
    response = requests.get(base_url1+url).text
    soup = BeautifulSoup(response, "lxml").title.text
    with open("usda/topics/" + soup + ".html", "w", encoding="utf-8") as f:
        f.write(response)
    print(soup)
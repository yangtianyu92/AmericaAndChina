#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 19:18
# @Email    : yangtianyu92@126.com
import requests
import re
from bs4 import BeautifulSoup

url_fda = "https://www.fda.gov/Safety/Recalls/default.htm"

header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'cache-control': 'max-age=0',
 'cookie': '_ga=GA1.2.129905225.1540258197; _gid=GA1.2.379007114.1545049326; '
           '_ceg.s=pjxmog; _ceg.u=pjxmog; '
           '_4c_=jVPNbts8EHyVDzwHEkn9Ub6lTdP20gIpPhQ9CStyZRORRIOk5RpB3j1LRXHRQ4CeTO6MZne44yd2PuDMdqIqK1HURaOkrG%2FYI14C2z0xb036WdiOGawrNagWhC76thY9KOBSVC0MjeQ1Zzfs96qjeFGKVqlCPN8wfdy%2Bf2LaGSQd0WZFVhIb5yR79IbOA9GYkG3LKymrjFS4rJRoG8I%2B33Zf796HT34k8BDjMezy%2FHw%2BZ4OBbO%2BW%2FAcMGC%2F5A2oYx5AbHOA0xuwQp9TRObLGftHR%2BNOe3LJvdO6tG93e6tCPRFhAazvjG6hdmDASuH3owViI1s0dpvkTBWY7wbhgRG9n8JetHF1PUu7onTnp%2BKY3obE0m8HF6muT%2B7vb7gOE1y6pEFYbW0siarsBI4QYUKcBqHKfDNFrueUOR7vgtfcXN%2BER9untVzkErw9%2FXWjYKXWjwgPuTyNE5y%2Fd7TCA9W9ee%2B%2FOAT3dPh48Kf7XpI27BP%2B0syEwPQgO6P3KSguhfQjFM1E3WVlnUjS7inOeRwiPOS2poyV1aexuW9H3U%2Bw9wmP4NKHf46wthg3alrcTQnAFhZRcNbrig1JcIQ49tobXUGLyZGPyuqUgPf4fe8cUufo1VP%2B%2FnyoK7muWCZBVWbZNQzKRgqbqkixwToyktUab%2Fi%2F%2FwKbryhZXtihrIcqmpcrKFuXGfn5%2BAQ%3D%3D',
 'upgrade-insecure-requests': '1',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

header2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'cookie': '',
 'referer': 'https://www.fda.gov/Safety/Recalls/default.htm',
 'upgrade-insecure-requests': '1',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

response = requests.get(url=url_fda, headers=header)

result_list = []
result_dict = {
    "Date": "",
    "Brand": "",
    "Report_Href": "",
    "Product_Description": "",
    "Reason_Problem": "",
    "Company": "",
}
a = re.findall('data\": \[(.*)]', response.text, re.DOTALL)
table = re.findall('\[(.*?)\]', a[0])[:-500]
for array in table:
    table_list = array.split(",")
    result_dict["Date"] = table_list[0].replace('\'', '')
    brand = re.findall('>(.*)<', table_list[1])
    if brand != []:
        result_dict["Brand"] = brand[0]
    else:
        result_dict["Brand"] = "null"
    result_dict["Report_Href"] = "https://www.fda.gov" + re.findall('href=\"(.*?)\">', table_list[1])[0]
    result_dict["Product_Description"] = table_list[2].replace('\'', '')
    try:
        result_dict["Reason_Problem"] = table_list[3].replace('\'', '')
        result_dict["Company"] = table_list[4].replace('\'', '')
    except:
        result_dict["Reason_Problem"] = "null"
        result_dict["Company"] = "null"
    result_list.append(result_dict)
    result_dict = {}

href_sum_list = [d["Report_Href"] for d in result_list]
len_href = len(href_sum_list)

for index, href in enumerate(href_sum_list):
    response_file = requests.get(url=href, headers=header2).text
    soup = BeautifulSoup(response_file,"lxml")
    title1 = soup.title.text
    title1 = re.sub('\W+', '', title1)
    title1 = ''.join(title1)[:100]
    print(title1)
    print("剩余数量: " + str(len_href-index))
    with open("fda/"+title1+".html", 'w', encoding="utf-8") as f:
        f.write(response_file)

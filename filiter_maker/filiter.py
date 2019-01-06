#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 21:02
# @Email    : yangtianyu92@126.com
from bs4 import BeautifulSoup
import re
import os


class ReInfo:
    def __init__(self, file):
        """
        初始化载入文档
        :param file: file-path
        """
        self.html_file = file
        self.soup = BeautifulSoup(file, "lxml")


    def get_title(self):
        """
        取标签
        :return:返回解析文档标题
        """
        return self.soup.title.text

    def get_info(self):
        """
        留以重载
        :return:返回网页各类信息，词典数据结构
        """
        pass


if __name__ == '__main__':
    with open('../cpsc/3MRecallsHardHatsDuetoShockHazardCPSCgov.html', 'r',encoding='utf-8') as f:
        file = f.read()

    ri = ReInfo(file)
    print(ri.get_title())



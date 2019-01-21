# -*- coding: utf-8 -*-
# Pytho 3.7

# Copyright © Taehong Kim, All rights reserved.

import ssl
import urllib.request
import bs4 # pip install bs4

# url 읽어오기
url = r"https://www.naver.com"
context = ssl._create_unverified_context()
html = urllib.request.urlopen(url, context=context)
# print(html.read())

# BeautifulSoup으로 html 문서 파싱
bs_obj = bs4.BeautifulSoup(html, "html.parser")
with open("test.html", "w") as f:
    f.write(str(bs_obj.contents))
# print(bs_obj)

# # TEST 1
# target = bs_obj.find("div", {"class":"area_links"})
# print(target)

# TEST 2
# target = bs_obj.findAll("a")
# for item in target :
#     print(item.get("href"))

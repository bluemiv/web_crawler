#!/usr/bin/python3
# -*- coding: utf-8 -*-


import re
import unittest


class Python3Test(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_count_str(self):
        greet = "Hello, World!"
        print("`o` count:", greet.count("o"))
        print("`l` count:", greet.count("l"))

    def test_find_str(self):
        greet = "Hello, Python"
        print(greet.find("Python"))  # 찾은 문자열의 첫번째 인덱스 반환
        print(greet.find("Java"))  # 찾는 문자열이 없으면 `-1` 을 반환

        foo = "Python2, Python3"
        print(foo.find("Python"))

    def test_re_search(self):
        a_tag = "<a href=\"https://www.naver.com\" target=\"_blank\">NAVER</a>"
        pattern = r"\"https?://[a-zA-Z0-9.]+\""

        search = re.search(pattern, a_tag)
        if search:
            print(search.group())
        else:
            print("Not found string. {}".format(search))

        pattern2 = r"\"((https?)://([a-zA-Z0-9.]+))\""
        search2 = re.search(pattern2, a_tag)
        if search2:
            print(search2.groups())
        else:
            print("Not found string. {}".format(search2))

    def test_re_match(self):
        foo = "Hello, Python3"
        pattern = r"[A-Z][a-z]+[0-9]"

        match = re.match(pattern, foo)
        if match:
            print("Find `Python3`")
        else:
            print("Not found `Python3`")


if __name__ == "__main__":
    unittest.main()

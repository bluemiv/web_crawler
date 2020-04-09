#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import tempfile
import unittest

import src.util.file_manager as fm


class FileMangerUnitTest(unittest.TestCase):

    def test_create_file(self):
        """_create_file() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # Not use encoding
            dest = os.path.join(tmp, "test.txt")
            self.assertTrue(fm._create_file(dest=dest, text="Hello, World!"))
            self.assertTrue(fm._create_file(dest=dest, text="Hello, World!", overwrite=True))
            self.assertRaises(RuntimeError, fm._create_file, dest=dest, text="Hello, World!", overwrite=False)

            # Use encoding
            dest = os.path.join(tmp, "test2.txt")
            self.assertTrue(fm._create_file(dest=dest, text="Hello, World!", encoding="utf-8"))
            self.assertTrue(fm._create_file(dest=dest, text="Hello, World!", encoding="utf-8", overwrite=True))
            self.assertRaises(RuntimeError, fm._create_file,
                              dest=dest, text="Hello, World!", encoding="utf-8", overwrite=False)

    def test_create_html(self):
        """create_html_file() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # Without `.html` and Not use encoding
            dest = os.path.join(tmp, "test")
            self.assertEqual(dest + ".html", fm.create_html_file(dest=dest, text="Hello, World!"))

            # Without `.html` and Use encoding
            dest = os.path.join(tmp, "test2")
            self.assertEqual(dest + ".html", fm.create_html_file(dest=dest, text="Hello, World!", encoding="utf-8"))

            # With `.html` and Not use encoding
            dest = os.path.join(tmp, "test3.html")
            self.assertTrue(dest, fm.create_html_file(dest=dest, text="Hello, World!"))

            # With `.html` and Use encoding
            dest = os.path.join(tmp, "test4.html")
            self.assertTrue(dest, fm.create_html_file(dest=dest, text="Hello, World!", encoding="utf-8"))

    def test_create_css(self):
        """create_css_file() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # Without `.html` and Not use encoding
            dest = os.path.join(tmp, "test")
            self.assertEqual(dest + ".css", fm.create_css_file(dest=dest, text="Hello, World!"))

            # Without `.html` and Use encoding
            dest = os.path.join(tmp, "test2")
            self.assertEqual(dest + ".css", fm.create_css_file(dest=dest, text="Hello, World!", encoding="utf-8"))

            # With `.html` and Not use encoding
            dest = os.path.join(tmp, "test3.css")
            self.assertTrue(dest, fm.create_css_file(dest=dest, text="Hello, World!"))

            # With `.html` and Use encoding
            dest = os.path.join(tmp, "test4.css")
            self.assertTrue(dest, fm.create_css_file(dest=dest, text="Hello, World!", encoding="utf-8"))

    def test_create_js(self):
        """create_css_file() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # Without `.html` and Not use encoding
            dest = os.path.join(tmp, "test")
            self.assertEqual(dest + ".js", fm.create_js_file(dest=dest, text="Hello, World!"))

            # Without `.html` and Use encoding
            dest = os.path.join(tmp, "test2")
            self.assertEqual(dest + ".js", fm.create_js_file(dest=dest, text="Hello, World!", encoding="utf-8"))

            # With `.html` and Not use encoding
            dest = os.path.join(tmp, "test3.js")
            self.assertTrue(dest, fm.create_js_file(dest=dest, text="Hello, World!"))

            # With `.html` and Use encoding
            dest = os.path.join(tmp, "test4.js")
            self.assertTrue(dest, fm.create_js_file(dest=dest, text="Hello, World!", encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

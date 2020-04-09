#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
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

    def test_get_new_filename(self):
        """_get_new_filename() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # rename test
            filepath = os.path.join(tmp, "test.txt")

            with open(filepath, "w") as f:
                f.write("Hello, World!")

            new_filepath = fm._get_new_filename(filepath)
            self.assertTrue(re.match(r"^{}{}[0-9]+test\.txt$".format(tmp, os.path.sep), new_filepath))

            # recursive rename test
            for n in range(0, 10):
                with open(os.path.join(tmp, "{}test.txt".format(n)), "w") as f:
                    f.write("Hello, World!")
            new_filepath = fm._get_new_filename(filepath)
            self.assertTrue(re.match(r"^{}{}[0-9]+test\.txt$".format(tmp, os.path.sep), new_filepath))

    def test_create_image(self):
        """create_image() Test"""
        with tempfile.TemporaryDirectory() as tmp:
            # Create image
            dest = os.path.join(tmp, "test.png")
            self.assertTrue(fm.create_image(dest=dest, byte_string=b"Hello, World!"))
            self.assertEqual(["test.png"], os.listdir(tmp))

            # Overwrite
            self.assertTrue(fm.create_image(dest=dest, byte_string=b"Hello, World!", overwrite=True))
            self.assertEqual(["test.png"], os.listdir(tmp))

            # Expected raise `RuntimeError` because of file is exists already.
            self.assertRaises(RuntimeError, fm.create_image, dest=dest, byte_string=b"Hello, World!", overwrite=False)

            # Rename and save
            self.assertTrue(fm.create_image(dest=dest, byte_string=b"Hello, World!", rename_save=True))
            self.assertEqual(2, len(os.listdir(tmp)))

    def test_remove(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Remove file
            filepath = os.path.join(tmp, "test.txt")
            with open(filepath, "w") as f:
                f.write("Hello, World!")
            self.assertTrue(fm.remove(filepath))

            # Remove Directory
            dir_path = os.path.join(tmp, "test")
            os.makedirs(dir_path)
            self.assertTrue(fm.remove(dir_path))
            
            # Remove not exists file.
            filepath = os.path.join(tmp, "not_exists_file.txt")
            self.assertTrue(fm.remove(filepath))


if __name__ == "__main__":
    unittest.main()

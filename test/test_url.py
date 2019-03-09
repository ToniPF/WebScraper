#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
import sys
import os
import unittest
from parameterized import parameterized
sys.path.append(os.getcwd() + '/webscaper')
from url import Url
from exceptions import InvalidUrlException


class TestUrl(unittest.TestCase):

    @parameterized.expand(
        [[None], [123], [""],
         ["w.fake-url.c"], ['www.fake-url'], ['www.fake-url.html']])
    def test_init(self, url_param):
        with self.assertRaises(InvalidUrlException):
            Url(url_param)

    @parameterized.expand([
        ['https://www.example.com'],
        ['https://cv.udl.cat/portal'],
        ['https://docs.python.org/3/library/unittest.html'],
        ['https://docs.unrealengine.com/en-US/Programming/Development/CodingStandard']])
    def test_equals(self, url_param):
        url = Url(url_param)
        self.assertEqual(url_param, url.url)

    @parameterized.expand([
        ['https://www.example.com'],
        ['https://cv.udl.cat/portal'],
        ['https://docs.python.org/3/library/unittest.html'],
        ['https://docs.unrealengine.com/en-US/Programming/Development/CodingStandard']])
    def test_str(self, url_param):
        url = Url(url_param)
        self.assertEqual(url_param, url.__str__())


if __name__ == '__main__':
    unittest.main()

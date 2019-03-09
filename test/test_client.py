#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8
import sys
import os
import unittest
from parameterized import parameterized
sys.path.append(os.getcwd() + '/webscaper')
from exceptions import IllegalArgumentError
from url import Url
from client import Client
from seeker import ISeeker
from messenger import IMessenger


class UrlStub(Url):
    def __init__(self):
        pass


class SeekerStub(ISeeker):
    def __init__(self):
        pass

    def seek(self, tree):
        pass


class MessengerStub(IMessenger):
    def __init__(self):
        pass

    def send(self, message):
        pass


class TestClient(unittest.TestCase):

    @parameterized.expand(
        [[None], [123], ["www.google.com"],
         ['https://cv.udl.cat/portal']])
    def test_init_url(self, url_param):
        with self.assertRaises(IllegalArgumentError):
            Client(url_param, SeekerStub())

    @parameterized.expand([
        [None], [123], ['Seeker'], [MessengerStub()],
        [0], [Url("https://cv.udl.cat/portal")]])
    def test_init_seeker(self, seeker_param):
        with self.assertRaises(IllegalArgumentError):
            Client(MessengerStub(), seeker_param)

    @parameterized.expand([
        [None], [123], ['Messenger'], [SeekerStub()],
        [0], [Url("https://cv.udl.cat/portal")]])
    def test_init_messenger(self, messenger_param):
        with self.assertRaises(IllegalArgumentError):
            Client(UrlStub(), SeekerStub(), messenger_param)


if __name__ == '__main__':
    unittest.main()

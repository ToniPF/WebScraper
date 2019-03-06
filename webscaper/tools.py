#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from url import Url
from exceptions import IllegalArgumentError


class Downloader(object):

    @staticmethod
    def download(url):
        """ This method is opening the connection to grab
            the html and then close the connection. """
        if not isinstance(url, Url):
            raise IllegalArgumentError("Downloader.download takes a Url as a parameter.")
        connection = urlopen(url.url)
        html = connection.read()
        connection.close()
        return html


class HTMLParser(object):

    html_parser = "html.parser"

    @staticmethod
    def parse(html):
        return BeautifulSoup(html, HTMLParser.html_parser)

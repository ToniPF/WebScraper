#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
# from bs4 import BeautifulSoup
from url import Url
from messenger import IMessenger, ConsoleMessenger
from seeker import ISeeker
from exceptions import IllegalArgumentError
from tools import Downloader, HTMLParser


class Client(object):

    html_parser = "html.parser"

    def __init__(self, url, seeker, out=ConsoleMessenger()):
        if not isinstance(url, Url):
            raise IllegalArgumentError("The Client's first argument should be a Url")
        if not isinstance(seeker, ISeeker):
            raise IllegalArgumentError("The Client's second argument should be a ISeeker")
        if not isinstance(out, IMessenger):
            raise IllegalArgumentError("The Client's third argument should be a IMessenger.")
        object.__init__(self)
        self.url = url
        self.seeker = seeker
        self.out = out

    def download_html(self):
        """ This method calls the downloader that handles
            the connection and grab de html.
        """
        return Downloader.download(self.url)

    def parse_html(self, html):
        """ This method calls the parser that
            takes de html object and convert it
            into a nested data structure.
        """
        return HTMLParser.parse(html)

    def run(self):
        html = self.download_html()
        page_tree = self.parse_html(html)
        products = self.seeker.seek(page_tree)
        self.out.send(products)

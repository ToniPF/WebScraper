#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from messenger import ConsoleMessenger


class Client(object):

    html_parser = "html.parser"

    def __init__(self, url, seeker, out=ConsoleMessenger()):
        object.__init__(self)
        self.url = url
        self.seeker = seeker
        self.out = out

    def download_html(self):
        """ This method is opening the connection
        to grab the html and then close the connection. """
        connection = urlopen(self.url)
        html = connection.read()
        connection.close()
        return html

    def run(self):
        html = self.download_html()
        page_tree = BeautifulSoup(html, self.html_parser)
        products = self.seeker.seek(page_tree)
        self.out.send(products)

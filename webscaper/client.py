#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from seeker import Seeker


class Client(object):

    html_parser = "html.parser"

    def __init__(self, url):
        object.__init__(self)
        self.url = url

    def download_html(self):
        """ This method is opening the connection
        to grab the html and then close the connection. """
        connection = urlopen(self.url)
        html = connection.read()
        connection.close()
        return html

    def debug_products(self, products):
        for product in products:
            print(product)
        print()

    def run(self):
        html = self.download_html()
        page_tree = BeautifulSoup(html, self.html_parser)
        products = Seeker().seek(page_tree)
        self.debug_products(products)

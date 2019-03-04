#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup


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

    def seek(self, tree):
        """ This is the method which handle the entire search. """
        containers = self._seek_containers(tree)
        products = self._seek_products(containers)
        return products

    def _seek_containers(self, tree):
        """ Getting all the items we want inspect
            from container/s. """
        items_container = []
        containers = tree.findAll('ul', 'goodlist_1')
        for container in containers:
            items_container += container.find_all('li')

        return items_container

    def _seek_products(self, item_containers):
        """ Getting the information we want from every product. """
        products = []
        for item_container in item_containers:
            price = item_container.find('div', 'priceitem')
            new_price = price.find('span', 'price')['oriprice']
            old_price = price.find('span', 'price_old')['oriprice']
            title = item_container.find('span', 'title').text
            products.append((title, new_price, old_price))

        return products

    def debug_products(self, products):
        for product in products:
            for element in product:
                print(element)
            print()

    def run(self):
        html = self.download_html()
        page_tree = BeautifulSoup(html, self.html_parser)
        products = self.seek(page_tree)
        self.debug_products(products)


if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    client = Client(my_url)
    client.run()

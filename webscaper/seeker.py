#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8
from product import Product


class Seeker(object):

    def __init__(self):
        object.__init__(self)

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

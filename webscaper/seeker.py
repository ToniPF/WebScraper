#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8
from product import Product


class Seeker(object):

    def __init__(self):
        object.__init__(self)

    def seek(self, tree):
        """ This is the method which handle the entire search.
            :param tree: data structure made from html.
            :return: A products list found in the html.
            :rtype: List
        """
        containers = self._seek_containers(tree)
        products = self._seek_products(containers)
        return products

    def _seek_containers(self, tree):
        """ Getting all the items we want inspect from container/s.
            :param tree: data structure made from a html.
            :return: A html elements list that contains the products information.
            :rtype: List
        """
        items_container = []
        containers = tree.findAll('ul', 'goodlist_1')
        for container in containers:
            items_container += container.find_all('li')

        return items_container

    def _seek_products(self, item_containers):
        """ Getting the information we want from every product.
            :return: The products list found in the html.
            :rtype: List
        """
        products = []
        for item_container in item_containers:
            price = item_container.find('div', 'priceitem')
            products.append(
                Product(
                    item_container.find('span', 'title').text,
                    price.find('span', 'price')['oriprice'],
                    price.find('span', 'price_old')['oriprice']
                )
            )
        return products

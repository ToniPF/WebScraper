#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8
from abc import ABC, abstractmethod
from product import Product


class ISeeker(ABC):
    @abstractmethod
    def seek(self, tree):
        raise NotImplementedError


class Seeker(ISeeker):

    info_unknown = 'unknown'

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
            title = self._get_title(item_container)
            if not title:
                continue
            price_container = item_container.find('div', 'priceitem')
            new_price = self._get_price(price_container, 'price')
            old_price = self._get_price(price_container, 'price_old')
            products.append(Product(title, new_price, old_price))
        return products

    def _get_title(self, item_container):
        """ Look for the product title.
            :param item_container: structure that contains the product information.
            :return: The product title.
            :rtype: str
        """
        content = None
        if item_container:
            content = item_container.find('span', 'title')
        if content:
            return content.text
        return None

    def _get_price(self, price_container, price_type):
        """ Look for the product info.
            :param price_container: structure that contains the product prices.
            :param price_type: str used to find the appropriate price.
            :return: The product price (new or old, depending on price_type parameter).
            :rtype: str
        """
        content = None
        if price_container:
            content = price_container.find('span', price_type)
        if content:
            return content['oriprice']
        return Seeker.info_unknown

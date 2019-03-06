#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8


class Product(object):

    def __init__(self, title, new_price, old_price):
        object.__init__(self)
        self.title = title
        self.new_price = new_price
        self.old_price = old_price

    def __str__(self):
        return "Title: {}\n New price: {}\n Old price {}"\
            .format(self.title, self.new_price, self.old_price)

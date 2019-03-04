#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8


class Client(object):

    def __init__(self, url):
        object.__init__(self)
        self.url = url

    def run(self):
        pass


if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    client = Client(my_url)
    client.run()

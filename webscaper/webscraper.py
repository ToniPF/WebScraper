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
        return containers

    def _seek_containers(self, tree):
        """ Getting all the items we want inspect
            from container/s. """
        items_container = []
        containers = tree.findAll('ul', 'goodlist_1')
        for container in containers:
            items_container += container.find_all('li')

        return items_container

    def run(self):
        html = self.download_html()
        page_tree = BeautifulSoup(html, self.html_parser)
        items_container = self.seek(page_tree)


if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    client = Client(my_url)
    client.run()

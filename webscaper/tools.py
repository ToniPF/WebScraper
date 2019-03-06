#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from urllib.request import urlopen
from url import Url
from exceptions import IllegalArgumentError


class Downloader(object):

    @staticmethod
    def download(url):
        """ This method is opening the connection to grab
            the html and then close the connection. """
        if not isinstance(Url, url):
            raise IllegalArgumentError("Downloader.download takes a Url as a parameter.")
        connection = urlopen(url.url)
        html = connection.read()
        connection.close()
        return html

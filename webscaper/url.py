#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
import re


class InvalidUrlException(Exception):
    """ Invalid url format. """


class Url(object):

    url_pattern = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

    def __init__(self, url):
        object.__init__(self)
        if not self.url_pattern.match(url):
            raise InvalidUrlException("Url: {} is not a valid url". format(url))
        self.url = url

    def __str__(self):
        return self.url

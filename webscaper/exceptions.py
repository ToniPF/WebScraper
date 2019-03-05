#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8


class InvalidUrlException(Exception):
    """ Invalid url format. """


class IllegalArgumentError(ValueError):
    """ Not allowed argument. """
    def __init__(self, msg):
        ValueError.__init__(self)
        self.msg = msg

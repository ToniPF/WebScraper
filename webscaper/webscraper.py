#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from client import Client

if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    client = Client(my_url)
    client.run()

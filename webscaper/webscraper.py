#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from client import Client
from seeker import Seeker
from url import Url

if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    test_url = Url("https://www.banggood.com/Flashdeals.html")
    print(test_url)

    seeker = Seeker()
    client = Client(my_url, seeker)
    client.run()

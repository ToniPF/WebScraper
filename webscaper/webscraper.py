#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from client import Client
from seeker import Seeker

if __name__ == '__main__':
    my_url = "https://www.banggood.com/Flashdeals.html"
    seeker = Seeker()
    client = Client(my_url, seeker)
    client.run()

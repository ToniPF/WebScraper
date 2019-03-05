#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
from client import Client
from seeker import Seeker
from urllib.error import HTTPError, URLError
from url import Url, InvalidUrlException


def main():
    target_url = "https://www.banggood.com/Flashdeals.html"

    try:
        seeker = Seeker()
        client = Client(target_url, seeker)
        client.run()
    except InvalidUrlException as e:
        print('Error: Url', target_url, 'has not a valid format.')
    except HTTPError as e:
        # This is a HTTP Error 403: Forbidden.
        print('ERROR: HTTP Error 403:', e.msg + '.', e.reason)
    except URLError as e:
        print('ERROR: Url Error:', e.reason + '.')


if __name__ == '__main__':
    main()

#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim set fileencoding=utf-8
import sys
import re
from client import Client
from seeker import Seeker
from urllib.error import HTTPError, URLError
from url import Url
from exceptions import IllegalArgumentError, InvalidUrlException
from seeker import ParameterizedSeeker
from search_builder import SearchBuilder, SearchParser


def main():

    target_url = Url("https://www.banggood.com/Flashdeals.html")

    try:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            if not re.match(r'(.)*\.data', filename):
                sys.stdout.write('Use: python3 {} <filename.data>\n'.format(sys.argv[0]))
                exit(1)

            data = SearchParser().read_data(filename)  # 'webscaper/test.data'
            builder = SearchBuilder(data)
            seeker = ParameterizedSeeker(builder)
        else:
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
    except IllegalArgumentError as e:
        print(e.msg)
    except (AttributeError, KeyError) as ex:
        print(ex)


if __name__ == '__main__':
    main()

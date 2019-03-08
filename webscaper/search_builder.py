#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8
import sys
import re

'''
container = ['ul', 'goodlist_1']
sub_container = ['li', '']
items = [[('span', 'title'), 'text'],
         [('div', 'priceitem'), ('span', 'price'), 'oriprice'],
         [('div', 'priceitem'), ('span', 'price_old'), 'oriprice']]
'''
conditional = "if content:\n"

item_content = "    content = content.find('{}','{}')\n"

text_select = "    ParameterizedSeeker.tmp_items.append(content.text)\n"

tag_select = "    ParameterizedSeeker.tmp_items.append(content['{}'])\n"

item_end = "else:\n" \
           "    ParameterizedSeeker.tmp_items.append('unknown')"

string_tab = "    "

#
################################################################################


def build_container_search():
    return "ParameterizedSeeker.containers = tree.find_all('{}', '{}')"\
        .format(container[0], container[1])


def build_sub_container_search():
    if not sub_container:
        return None
    return "ParameterizedSeeker.sub_containers += container.find_all('{}', '{}')"\
        .format(sub_container[0], sub_container[1])


def build_items_search():
    items_list, item_info = [], []
    for item in items:
        find_items_info = ''
        for cnt, token in enumerate(item):
            find_items_info += add_conditional(cnt)
            if isinstance(token, tuple):
                find_items_info += item_content.format(token[0], token[1])
            else:
                if token.__eq__(''):
                    break
                elif token.__eq__('text'):
                    find_items_info += text_select
                    break
                else:
                    find_items_info += tag_select.format(token)
                    break
        find_items_info += item_end
        items_list.append(find_items_info)
    return items_list


def add_conditional(cnt):
    indent_depth = add_tabs(cnt)
    return indent_depth + conditional + indent_depth


def add_tabs(indent_depth):
    tabs = ''
    for i in range(indent_depth):
        tabs += string_tab
    return tabs

#
################################################################################


class SearchParams(object):

    def __init__(self, url, container, items, subcontainer=[]):
        self.url = url
        self.container = container
        self.items = items
        self.subcontainer = subcontainer

    def __str__(self):
        return "url: {}\ncontainer:{}\nsubcontainer{}\nitems{}\n"\
            .format(self.url, self.container, self.subcontainer, self.items)


class SearchParser(object):

    URL = re.compile('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    CONTAINER = re.compile(r'^\s*\t*container\s*=\s*.*')
    SUBCONTAINER = re.compile(r'^\s*\t*subcontainer\s*=\s*.*')
    ITEM = re.compile(r'^\s*\t*item\s*=\s*.*')

    def read_data(self, filename):
        url, container_line, sub_container_line, items_lines = '', '', '', []
        with open(filename, 'r') as file:
            reader = (line for line in map(str.strip, file) if line and line[0] != '*')
            for line in reader:
                print(line)
                if SearchParser.URL.match(line):
                    url = line
                elif SearchParser.CONTAINER.match(line):
                    container_line = line
                elif SearchParser.SUBCONTAINER.match(line):
                    sub_container_line = line
                elif SearchParser.ITEM.match(line):
                    items_lines.append(line)

            if self.missing_values(url, container_line, items_lines):
                self.print_data_file_format()
                sys.exit(1)

            container = self.parse_container(container_line)
            sub_container = self.parse_container(sub_container_line)
            items = self.parse_items(items_lines)
        if id(sub_container) == id(''):
            return SearchParams(url, container, items)
        return SearchParams(url, container, items, sub_container)

    def parse_items(self, items_lines):
        items = []
        for line in items_lines:
            items.append(self.parse_item(line))
        return items

    def parse_item(self, items_line):
        item_body_line = self.eliminate_head(items_line)
        item_body_line, item_tag = self.get_item_chunck(item_body_line, '>')
        item_body = item_body_line.split('|')
        new_item = []
        for token in item_body:
            item = tuple(it.strip() for it in token.split(','))
            if len(item) != 2:
                self.print_data_file_format()
                sys.exit(1)
            new_item.append(item)
        item_tag = item_tag.strip()
        if id(item_tag) != id('-'):
            new_item.append(item_tag)
        return new_item

    def parse_container(self, container):
        data = container.split('=')
        if len(data) != 2:
            self.print_data_file_format()
            sys.exit(1)
        new_container = data[1].split(',')
        return new_container

    def get_item_chunck(self, items_line, delimiter):
        data = items_line.split(delimiter)
        self.check_split_data(data)
        return data[0], data[1]

    def eliminate_head(self, line):
        data = line.split('=')
        self.check_split_data(data)
        return data[1].strip()

    def check_split_data(self, data):
        if len(data) != 2:
            self.print_data_file_format()
            sys.exit(1)

    def missing_values(self, url, container_line, items_lines):
        empty_id = id('')
        return id(url) == empty_id or id(container_line) == empty_id or len(items_lines) == 0

    def print_data_file_format(self):
        print('#####################################\n')
        print('File format:')
        print('https://www.example.com')
        print('container = tag, class')
        print('subcontainer = tag, class')
        print('item = tag, class | tag, class | ...\n')
        print('#####################################')


params = SearchParser().read_data('webscaper/test.data')
print(params.__str__())

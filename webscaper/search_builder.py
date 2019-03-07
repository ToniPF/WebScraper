#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8


container = ['ul', 'goodlist_1']
sub_container = ['li', '']
items = [[('span', 'title'), 'text'],
         [('div', 'priceitem'), ('span', 'price'), 'oriprice'],
         [('div', 'priceitem'), ('span', 'price_old'), 'oriprice']]

conditional = "if content:\n"

item_content = "    content = content.find('{}','{}')\n"

text_select = "    ParameterizedSeeker.tmp_items.append(content.text)\n"

tag_select = "    ParameterizedSeeker.tmp_items.append(content['{}'])\n"

item_end = "else:\n" \
           "    ParameterizedSeeker.tmp_items.append('unknown')"

string_tab = "    "


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

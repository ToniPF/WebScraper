#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8


container = ['ul', 'goodlist_1']
sub_container = ['li', '']
items = [[('span', 'title'), 'text'],
         [('div', 'priceitem'), ('span', 'price'), 'oriprice'],
         [('div', 'priceitem'), ('span', 'price_old'), 'oriprice']]

item_content = "if content:\n" \
    "    content = content.find('{}','{}')\n"

text_select = "if content:\n" \
    "    ParameterizedSeeker.tmp_items.append(content.text)\n"

tag_select = "if content:\n" \
    "    ParameterizedSeeker.tmp_items.append(content['{}'])\n"

item_end = "else:\n" \
           "    ParameterizedSeeker.tmp_items.append('unknown')\n" \
           "ParameterizedSeeker.items.append(ParameterizedSeeker.tmp_items)\n" \
           "ParameterizedSeeker.tmp_items = []"

string_tab = '    '


def build_container_search():
    return "ParameterizedSeeker.containers = tree.find_all('{}', '{}')"\
        .format(container[0], container[1])


def build_sub_container_search():
    if not sub_container:
        return None
    return "ParameterizedSeeker.sub_containers += container.find_all('{}', '{}')"\
        .format(sub_container[0], sub_container[1])


def build_items_search():
    items_list = []
    for item in items:
        find_items_info, cnt = '', 0
        for token in item:
            if isinstance(token, tuple):
                add_tabs(find_items_info, cnt)
                find_items_info += item_content.format(token[0], token[1])
            else:
                if token.__eq__(''):
                    break
                elif token.__eq__('text'):
                    add_tabs(find_items_info, cnt)
                    find_items_info += text_select
                    break
                else:
                    add_tabs(find_items_info, cnt)
                    find_items_info += tag_select.format(token)
                    break
        find_items_info += item_end
        items_list.append(find_items_info)
    return items_list


def add_tabs(item_info, tabs_cnt):
    for i in range(tabs_cnt):
        item_info += string_tab

    return item_info

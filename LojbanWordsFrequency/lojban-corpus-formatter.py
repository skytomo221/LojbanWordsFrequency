# -*- coding: utf-8 -*-
import re

file_in_name = 'corpus.txt'
file_out_name = 'output.txt'

text_len = 0
text = ''

def my_print(memo):
    print(str.format('{:<30}: {:>10} {:>10.2f}%', memo, len(text), float(len(text)) / text_len * 100))

with open(file_in_name, encoding='UTF-8') as file_in:
    with open(file_out_name, 'w', encoding='UTF-8') as file_out:
        text = file_in.read()
        text_len = len(text)
        my_print('Length')
        text = re.sub(r'^.*<.*>', '', text, flags=re.MULTILINE)
        text = re.sub(r'\[.*\] <.*>', '', text)
        my_print('Delete chats')
        text = re.sub(r'-header(.|\s)*?start-+', '', text)
        my_print('Delete headers and starts')
        text = re.sub(r'-end-+', '', text)
        my_print('Delete ends')
        text = re.sub(r'(http|https)://([\w-]+\.)+[\w-]+(/[\w\-\./\?%&=]*)?', '', text)
        my_print('Delete URLs')
        text = re.sub(r'[^A-Za-z\' ]', '', text)
        my_print('Delete non-alphabet')
        text = re.sub(r'\w*h\w*', '', text)
        my_print('Delete words containing h')
        text = re.sub(r'(^|\W)[A-Z][a-z]+', '', text)
        my_print('Delete uppercase words')
        text = text.lower()
        print('Convert text to lowercase')
        file_out.write('\n'.join(map(str, text.split())))
        my_print('Compeleted')

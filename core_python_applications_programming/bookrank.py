#!/usr/bin/env python
# coding:utf-8
from atexit import register
from re import compile
from threading import Thread
from time import ctime

import requests

REGEX = compile('#([\d,]+) in Books')
AMZN = 'https://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    _url = '%s%s' % (AMZN, isbn)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    page = requests.get(_url, headers=headers)
    data = page.text
    if page.status_code == 200:
        return REGEX.findall(data)[0]
    else:
        return "unknown"

def _showRanking(isbn):
    print('- %r randked %s' %(ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
       # _showRanking(isbn)
       Thread(target=_showRanking, args=(isbn,)).start()

@register # atexit模块主要的作用就是在程序即将结束之前执行的代码, atexit.register 注册函数
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    _main()
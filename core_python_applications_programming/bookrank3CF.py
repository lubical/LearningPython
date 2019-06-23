#!/usr/bin/env python
from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen, Request

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs={
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}
def getRanking(isbn):
    # 伪装成浏览器访问，直接访问的话会拒绝
    myUrl = '{0}{1}'.format(AMZN, isbn)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    # 构造请求
    req = Request(myUrl, headers=headers)
    with uopen(req) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')

def _main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(
                ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s' % (ISBNs[isbn], ranking))
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
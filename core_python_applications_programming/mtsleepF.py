#!/usr/bin/env python
from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()
lock = Lock()

def loop_without_lock(nsec):
    myname = currentThread().name
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print(' (remaining: %s)' % (remaining or 'NONE'))

def loop(nsec):
    myname = currentThread().name
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)
    with lock:    # 等价于第一句添加lock.acquire(),最后一句添加lock.release()
        remaining.remove(myname)
        print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
        print(' (remaining: %s)' % (remaining or 'NONE'))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

    # for pause in loops:
    #     Thread(target=loop_without_lock, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()

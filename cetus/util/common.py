# -*- coding:utf-8 -*-
__author__ = 'baohua'

VERSION = '0.1'
LOG_FILE = '/var/log/cetus.log'


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

if __name__ == '__main__':
    import doctest
    doctest.testmod()
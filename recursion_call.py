#!/usr/bin/env/ python3

import sys

def recursion(n):
    x = 1
    n = n-x
    print('when n = {}, parameter:{}, local var:{}'.format(n, hex(id(n)), hex(id(x))))
    if n>0: recursion(n)
    print('Run once')

if __name__ == '__main__':
    recursion(int(sys.argv[1]))
    print('END')

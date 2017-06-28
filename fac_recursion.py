#!/usr/bin/env/ python3

import sys

def fac_recursion(n):
    if n == 0: return 1
    return fac_recursion(n-1)*n

if __name__ == '__main__':
    print(fac_recursion(int(sys.argv[1])))

#!/usr/bin/env/ python3

import sys

def fac_interation(n):
    if n == 0: return 1
    s = 1
    for i in range(1, n+1): s = s * i
    return s

if __name__ == '__main__':
    print(fac_interation(int(sys.argv[1])))

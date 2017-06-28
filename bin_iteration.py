#!/bin/usr/env/ python3

import sys

def bin_(n, m):
    if (n==m) or (m==0): return 1
    s1, s2 = 1.0, 1.0
    for i in range(1, m+1):
        s1 *= i
        s2 *= i+(n-m)
    return s2/s1

if __name__ == '__main__':
    print(bin_(int(sys.argv[1]), int(sys.argv[2])))

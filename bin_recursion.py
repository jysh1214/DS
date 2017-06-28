#!/usr/bin/env/ python3

import sys

def bin(n, m):
    if (n==m) or (m==0): return 1
    else: return bin(n-1, m)+bin(n-1, m-1)

if __name__ == '__main__':
    print(bin(int(sys.argv[1]), int(sys.argv[2])))

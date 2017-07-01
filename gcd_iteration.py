#!/usr/bin/env/ python3

import sys

def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if (a%i==0) and (b%i==0): return i

if __name__ == '__main__':
    print(gcd(int(sys.argv[1]), int(sys.argv[2])))

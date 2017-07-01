#!/usr/bin/env/ python3

import sys

def gcd(a, b):
    if a%b == 0: return b
    else: return gcd(b, a%b)

if __name__ == '__main__':
    print(gcd(int(sys.argv[1]), int(sys.argv[2])))

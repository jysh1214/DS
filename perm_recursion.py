#!/usr/bin/env/ python3

import sys

def perm(list, i, n):
    if i == n:
        for j in range(0, n): print(list[j],end='')
        print()
    else:
        for j in range(i, n):
            list[i], list[j] = list[j], list[i]
            perm(list, i+1, n)
            list[j], list[i] = list[i], list[j]

if __name__ == '__main__':
    i = int(sys.argv[1])
    n = int(sys.argv[2])
    list = [x+1 for x in range(0, n)]
    perm(list, i, n)

#!/usr/bin/env/ python3

def fac_recursion(n):
    if n == 0: return 1
    return fac_recursion(n-1)*n

if __name__ == '__main__':
    print(fac_recursion(5))

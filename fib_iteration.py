#!/usr/bin/env/ python3

def fib_iteration(n):
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    print(fib_iteration(10))

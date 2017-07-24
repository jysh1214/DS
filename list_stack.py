#!/usr/bin/env/ python3
"""
stack length = 7
"""
def push(stack, item):
    if len(stack) == 7:
        print('The stack is full.')
    else:
        stack.append(item)

def pop(stack):
    if len(stack) == 0:
        print('The stack is empty.')
    else:
        stack.pop() #stack.remove(stack[-1])

stack = [1, 1, 1]
while True:
    action = input('>>>Input(0:push, 1:pop):')
    if action == '0':
        push(stack, 1)
    else:
        pop(stack)
    print(stack)

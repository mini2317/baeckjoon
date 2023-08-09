from collections import deque
n = int(input())
infixNotation = input()
stack = deque()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = dict((alphabet[i], int(input())) for i in range(n))
for token in infixNotation:
    if token in '*/+-':
        b = stack.pop()
        a = stack.pop()
        if token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(a / b)
        elif token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
    else:
        stack.append(numbers[token])
print('%.2f' % stack[-1])
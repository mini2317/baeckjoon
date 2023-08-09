from collections import deque
infixNotation = input()
stack = deque()
postfixNotation = []
token = 0
for one in infixNotation:
    if one == ')':
        while stack[-1] != '(':
            postfixNotation += stack.pop()
        stack.pop()
    elif one == '(':
        stack.append('(')
    elif one in '*/':
        while len(stack) > 0:
            if stack[-1] in '+-(': break
            postfixNotation += stack.pop()
        stack.append(one)
    elif one in '+-':
        for i in range(len(stack)):
            if stack[-1] in '(': break
            postfixNotation += stack.pop()
        stack.append(one)
    else:
        postfixNotation *= 10
        postfixNotation += int(infixNotation)
for i in range(len(stack)): postfixNotation.append(stack.pop())
print(postfixNotation)
stack = deque()
for token in postfixNotation:
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
        stack.append(token)
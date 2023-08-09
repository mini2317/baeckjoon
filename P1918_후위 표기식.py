from collections import deque
infixNotation = input()
stack = deque()
postfixNotation = ''
for token in infixNotation:
    if token == ')':
        while stack[-1] != '(':
            postfixNotation += stack.pop()
        stack.pop()
    elif token == '(':
        stack.append('(')
    elif token in '*/':
        while len(stack) > 0:
            if stack[-1] in '+-(': break
            postfixNotation += stack.pop()
        stack.append(token)
    elif token in '+-':
        for i in range(len(stack)):
            if stack[-1] in '(': break
            postfixNotation += stack.pop()
        stack.append(token)
    else:
        postfixNotation += token
for i in range(len(stack)): postfixNotation += stack.pop()
print(postfixNotation)
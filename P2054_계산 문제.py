from collections import deque

FAILED = -1

def toPostfix(f):
    stack = deque()
    rst = []
    temp = ''
    for i in f:
        if i == '*':
            if str(int(temp)) == temp:
                rst.append(int(temp))
                temp = ''
            else:
                return FAILED
            for _ in range(len(stack)):
                if stack[-1] in '+-(': break
                rst.append(stack.pop())
            stack.append(i)
        elif i in '+-':
            if str(int(temp)) == temp:
                rst.append(int(temp))
                temp = ''
            else:
                return FAILED
            for _ in range(len(stack)):
                if stack[-1] in '(': break
                rst.append(stack.pop())
            stack.append(i)
        else:
            temp += i
    if temp:
        if str(int(temp)) == temp:
                rst.append(int(temp))
                temp = ''
        else:
            return FAILED
    for _ in range(len(stack)): rst.append(stack.pop())
    return rst

def solvePostfix(lf):
    stack = lf[:]
    for token in lf:
        if type(token) == str:
            b = stack.pop()
            a = stack.pop()
            if token == '*':
                stack.append(a * b)
            elif token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
        else:
            stack.append(token)
    return stack[-1]

num = input()
n = len(num) - 1
OPERATOR = 's+-*'
rst = []
for i in range(4 ** n):
    formula = num[0]
    if i % 4 : formula += OPERATOR[i % 4]
    j = 1
    d = i // 4
    while d // 4 != 0:
        formula += num[j]
        now = d % 4
        if now : formula += OPERATOR[now]
        d //= 4
        j += 1
    now = d % 4
    formula += num[j]
    if now : formula += OPERATOR[now]
    formula += num[j + 1 : ]
    post = toPostfix(formula)
    if post != FAILED:
        if solvePostfix(post) == 2000: rst.append(formula)
print(*sorted(rst))
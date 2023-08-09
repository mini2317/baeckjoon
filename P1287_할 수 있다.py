from collections import deque
FAILED = 'ROCK'
formula = input()
def getPost(formula):
    rst = []
    stack = deque()
    leftCnt = 0
    rightCnt = 0
    for i in range(len(formula)):
        token = formula[i]
        if token == '(':
            leftCnt += 1
            stack.append('(')
        elif token == ')':
            rightCnt += 1
            if formula[i - 1] == '(': return FAILED
            for _ in range(len(stack)):
                temp = stack.pop()
                if temp == '(': break
                rst.append(temp)
        elif token in '*/':
            for _ in range(len(stack)):
                if stack[-1] in '+-(': break
                rst.append(stack.pop())
            stack.append(token)
        elif token in '+-':
            for _ in range(len(stack)):
                if stack[-1] == '(': break
                rst.append(stack.pop())
            stack.append(token)
        else:
            if rst:
                if formula[i - 1] == ')': return FAILED 
                if formula[i - 1] in '+-*/(': rst.append('')
                if formula[i - 1] != '0':
                    rst[-1] += token
                else:
                    return FAILED
            else:
                rst.append(token)
    if leftCnt != rightCnt: return FAILED
    for _ in range(len(stack)): rst.append(stack.pop())
    return rst

def calculate(postfixFomula):
    try:
        stack = deque()
        for token in postfixFomula:
            if token in '*/+-':
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a // b)
                elif token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
            else:
                stack.append(token)
        return stack[-1]
    except:
        return FAILED
post = getPost(formula)
if post != FAILED:
    print(calculate(post))
else:
    print(FAILED)
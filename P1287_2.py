expr = input()

def innerEval(expr):
    operator = ["+","-","/","*"]
    marker = -1
    stack = []
    minus = -1
    if expr == "":
        return "ROCK"
    for j in range(len(expr)):
        if minus == -1:
            if expr[j] == "(":
                minus = j
            elif expr[j] in operator:
                if (expr[j] != '-' and j == 0) or j == len(expr)-1:
                    return "ROCK"
                if j < len(expr) - 1:
                    if expr[j+1] in operator:
                        return "ROCK"

                nowNum = expr[marker+1:j]
                marker = j
                if stack != []:
                    if stack[-1] in operator and nowNum =='':
                        return "ROCK"
                if nowNum != '':
                    if str(int(nowNum)) != nowNum:
                        return 'ROCK'
                    if stack != []:
                        if stack[-1] in "*/":
                            oper = stack.pop()
                            a = stack.pop()
                            if a == "0" and oper == "/":
                                return "ROCK"
                            stack.append(int(eval((str(a) + oper + nowNum).replace("/","//"))))

                        else:
                            stack.append(int(nowNum))
                    else:
                        stack.append(int(nowNum))
                stack.append(expr[j])
        else:
            if expr[j] == ")":
                nowNum = expr[minus+1:j]
                if stack != []:
                    if stack[-1] in "*/":
                        oper = stack.pop()
                        a = stack.pop()
                        if a == "0" and oper == "/":
                            return "ROCK"
                        stack.append(int(eval((str(a) + oper + nowNum).replace("/","//"))))
                    else:
                        stack.append(int(nowNum))
                else:
                    stack.append(int(nowNum))
                minus = -1
                marker = j
    nowNum = expr[marker+1:]
    if nowNum != '':
        if str(int(nowNum)) != nowNum:
            return 'ROCK'
        if stack != []:
            if stack[-1] in "*/":
                oper = stack.pop()
                a = stack.pop()
                if a == "0" and oper == "/":
                    return "ROCK"
                stack.append(int(eval((str(a) + oper + nowNum).replace("/","//"))))
            else:
                stack.append(int(nowNum))
        else:
            stack.append(int(nowNum))
    removed = 0
    for j in range(len(stack)):
        idx = j - removed
        if len(stack) == 1:
            break
        if isinstance(stack[idx],str):
            if stack[idx] in "+-":
                if (stack[idx] != '-' and idx == 0) or idx == len(stack)-1:
                    return "ROCK"
                if stack[idx] == '-' and idx == 0:
                    a = 0
                    oper = stack.pop(idx)
                    b = stack.pop(idx)
                    removed += 1
                    stack.insert(idx,eval(str(a) + oper + str(b)))
                else:
                    a = stack.pop(idx-1)
                    oper = stack.pop(idx-1)
                    b = stack.pop(idx-1)
                    removed += 2
                    stack.insert(idx-1,eval(str(a) + oper + str(b)))
    return stack[0]

def superEval(expr):
    try:
        openStack = []
        remove = 0
        for i in range(len(expr)):
            idx = i - remove
            if expr[idx] == "(":
                openStack.append(idx)
            elif expr[idx] == ")":
                a = openStack.pop()
                nowExpr = expr[a+1:idx]
                rst = innerEval(nowExpr)
                if rst < 0:
                    rst = f'({rst})'
                if rst == "ROCK":
                    return "ROCK"
                expr = expr[:a] + str(rst) + expr[idx+1:]
                remove += len(str(nowExpr))-len(str(rst)) + 2
        if openStack != []:
            return "ROCK"
        return innerEval(expr)
    except Exception as e:
        return 'ROCK'
print(superEval(expr))
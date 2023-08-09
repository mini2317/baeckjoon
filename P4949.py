def checker(s):
    stack= []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        if len(stack) > 0:
            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        elif i == ")" or i == "]":
            return False
    return not stack
while True:
    s = input()
    if s == ".":break
    print("yneos"[not checker(s)::2])
import sys
stack=[]
input=sys.stdin.readline
for _ in '.'*int(input()):
    arg=input().split()
    if arg[0] == 'push':stack.append(int(arg[1]))
    elif arg[0] == 'pop':print(stack.pop()if stack else -1)
    elif arg[0] == 'size':print(len(stack))
    elif arg[0] == 'empty':print(int(not stack))
    else:print(stack[-1]if stack else -1)
    
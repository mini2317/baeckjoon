a,b=int(input()),int(input())
p = (a//100)*100+b
print(str(p-p%b if p%b else (a//100)*100)[-2:])
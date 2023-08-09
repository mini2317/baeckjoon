
from math import sin
A,B,C=map(int,input().split())
x=C/A
for i in range(31):
    for _ in range(10):if A*x+B*sin(x)-C>0: x-=10**(-i)
    x+=10**(-i)
print(x)
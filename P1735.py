from math import gcd
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[0]*b[1]+b[0]*a[1]
d=a[1]*b[1]
g=gcd(c,d)
c//=g
d//=g
print(c,d)
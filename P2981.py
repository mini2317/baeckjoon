from math import gcd
l = int(input())
s = sorted(int(input()) for i in '.'*l)
dist = [s[i]-s[i-1] for i in range(1,l)]
t = gcd(*dist)
m = set()
r = t
for i in range(2,int(t**0.5)+1):
    if t%i==0:
        m.add(t//i)
        m.add(i)
if r!=1:
    m.add(t//r)
    m.add(r)
m.add(t)
m.remove(1)
print(*sorted(m))
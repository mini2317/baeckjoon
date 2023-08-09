from math import gcd
X1,Y1,X2,Y2 = 0,1,2,3
line1,line2 = map(int,input().split()),map(int,input().split())
a1 = (line1[X2] - line1[X1], line1[Y2] - line1[Y1])
g = gcd(*a1)
a1[0] //= g
a1[1] //= g
b1 = line1[X1],line1[Y1]
a2 = (line2[X2] - line2[X1], line2[Y2] - line2[Y1])
g = gcd(*a2)
a2[0] //= g
a2[1] //= g
b2 = line2[X1],line2[Y1]
if a1 == a2 and a1:
    print(0)
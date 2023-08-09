import math
X,Y = map(int,input().split())
Z = 100*Y//X
V = math.ceil((100*Y-(Z+1)*X)/(Z-99)) if Z != 99 else -1
print(V if V > 0 else -1)
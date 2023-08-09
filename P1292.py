from math import ceil
A,B = map(int,input().split())
print(sum((ceil(((8*i-1)**0.5-1)/2)) for i in range(1,1001)[A-1:B]))
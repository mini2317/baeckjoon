from math import gcd
input()
g=list(map(int,input().split()))
print('\n'.join(map(lambda x:f"{g[0]//gcd(g[0],x)}/{x//gcd(g[0],x)}",g[1:])))
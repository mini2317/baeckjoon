from math import log2
def Sxor(n):
    if n == 0 : return 0
    l = int(log2(n)) + 1
    rst = 0
    for i in range(l):
        d = 2**i if i >= 1 else 0
        rst += (max(0,(n+1)%2**(i+1) - d)%2)*2**i
        print(i,(max(0,n%2**(i+1) - d)%2)*2**i)
    return rst
A,B = map(int,input().split())
print(Sxor(A) ^ Sxor(B))
'''
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
'''
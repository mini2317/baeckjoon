from math import log2
def Sf(x):
    lx = int(log2(x))
    rst = x+1-2**lx
    for i in range(lx):
        rst += (x+1)//2**(i+1)*2**i + (x+1)%2**(i+1)-2**i
        print((x+1)//2**(i+1)*2**i + (x+1)%2**(i+1)-2**i)
    print("==")
    return rst
print(Sf(int(input())))
#A,B = map(int,input().split())
#print(Sf(B) - Sf(A-1))
'''
0  0000 0 0
1  0001 1 1
2  0010 1 2
3  0011 2 4
4  0100 1 5
5  0101 2 7
6  0110 2 9
7  0111 3 12
8  1000 1 13
9  1001 2 15
10 1010 2 17
11 1011 3 20
12 1100 2 22
13 1101 3 25
14 1110 3 28
15 1111 4 32
'''
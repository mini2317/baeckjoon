import sys, math
input = sys.stdin.readline

def getSurface(p, L):
    rst = 0
    for i in range(L):
        rst += p[i][0] * p[(i+1)%L][1] - p[(i+1)%L][0] * p[i][1]
    return abs(rst)/2

def getTriangleSurface(a,b,c):
    return abs((b[1] - c[1]) * a[0] + (c[1] - a[1]) * b[0] + (a[1] - b[1]) * c[0])/2

def check(p, A, B, N, M, Asur, Bsur):
    rst1, rst2 = 0, 0
    for i in range(max(N,M)):
        triangle1 = getTriangleSurface((A[2*i],A[2*i+1]),(A[(2*i+2)%(2*N)],A[(2*i+3)%(2*N)]),p) if i < N else 1
        triangle2 = getTriangleSurface((B[2*i],B[2*i+1]),(B[(2*i+2)%(2*M)],B[(2*i+3)%(2*M)]),p) if i < M else 1
        rst1 += triangle1 if i < N else 0
        rst2 += triangle2 if i < M else 0
    return rst1 == Asur and rst2 != Bsur

N, M, K = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
p = tuple(map(int, input().split()))
rst = K
Asurface = 0
for i in range(N): Asurface += A[2*i] * A[(2*i+3)%(2*N)] - A[(2*i+2)%(2*N)] * A[2*i+1]
Asurface = abs(Asurface)/2
Bsurface = 0
for i in range(M): Bsurface += B[2*i] * B[(2*i+3)%(2*M)] - B[(2*i+2)%(2*M)] * B[2*i+1]
Bsurface = abs(Bsurface)/2
for i in range(K):rst -= check((p[2*i],p[2*i+1]), A, B, N, M, Asurface, Bsurface)
print(rst if rst else 'YES')

'''
8 5 8
2 5 1 6 -2 6 -4 5 -5 2 -1 0 2 1 3 3
0 5 -4 4 -2 1 1 1 2 3
-4 2 -3 5 -3 2 1 5 2 2 -2 5 -1 5 2 4
'''
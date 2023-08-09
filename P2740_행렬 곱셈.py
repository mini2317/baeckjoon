n, m = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [tuple(map(int, input().split())) for _ in range(m)]
c = [[0 for _ in range(k)] for __ in range(n)]
for i in range(n):
    for j in range(m):
        for l in range(k):
            c[i][l] += a[i][j] * b[j][l]
for i in range(n) : print(*c[i])
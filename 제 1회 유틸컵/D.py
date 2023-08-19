import sys
input = sys.stdin.readline
n = int(input())
field = [list(map(int, input().split())) for i in range(n)]
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        field[q[1] - 1].insert(0, field[q[1] - 1].pop())
    else:
        a = []
        for i in range(n):
            a.append([field[n - j - 1][i] for j in range(n)])
        field = a
for i in field: print(*i)
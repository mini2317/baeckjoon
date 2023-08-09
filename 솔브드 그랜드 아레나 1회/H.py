import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
sum_ = [[0] * n, [0] * m]
for _ in range(q):
    query = [*map(int, input().split())]
    if query[0] == 1:
        sum_[0][query[1] - 1] += query[2]
    else:
        sum_[1][query[1] - 1] += query[2]
for i in range(n):
    for j in range(m):
        print(sum_[0][i] + sum_[1][j], end=' ')
    print()
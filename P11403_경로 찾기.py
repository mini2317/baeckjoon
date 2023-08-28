import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
n = int(input())
adj = [list(map(int, input().split())) for i in range(n)]
rst = []
for i in range(n):
    rst.append([0] * n)
    queue = deque()
    for j in range(n):
        if adj[i][j] == 1:
            queue.append(j)
            rst[-1][j] = 1
            while queue:
                now = queue.popleft()
                for k in range(n):
                    if adj[now][k] == 1 and rst[-1][k] == 0:
                        queue.append(k)
                        rst[-1][k] = 1
for i in range(n): print(*rst[i])
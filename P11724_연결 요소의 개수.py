from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
numSet = set(range(2, n + 1))
queue = deque([1])
cnt = 1
while numSet:
    while queue:
        a = queue.popleft()
        for i in range(1, n + 1):
            if graph[a][i] != 0 and i in numSet:
                queue.append(i)
                numSet.remove(i)
    if numSet:
        temp = tuple(numSet)[0]
        queue.append(temp)
        numSet.remove(temp)
    else: break
    cnt += 1
print(cnt)
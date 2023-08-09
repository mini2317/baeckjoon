from collections import deque
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
graph = [[0]*W for _ in range(H)]
queue = deque()
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for y in range(H):
    row = list(map(int, input().split()))
    for x in range(W):
        graph[y][x] = row[x]
        if row[x] == 1:
            queue.append((y, x))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((ny, nx))

if any(graph[y][x] == 0 for y in range(H) for x in range(W)):
    print(-1)
else:
    print(max(graph[y][x] for y in range(H) for x in range(W)) - 1)

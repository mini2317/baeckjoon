import sys
sys.setrecursionlimit(300)
def input(): return sys.stdin.readline().strip()
n = int(input())
picture = [list(input()) for i in range(n)]
visited = [[0] * n for i in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
normal = 0
weak = 0
def dfs(x, y, color):
    global visited, picture
    visited[y][x] = True
    if picture[y][x] == 'R':
        picture[y][x] = 'G'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if picture[ny][nx] == color and not visited[ny][nx]:
                dfs(nx, ny, color)
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            normal += 1
            dfs(x, y, picture[y][x])
visited = [[0] * n for i in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            weak += 1
            dfs(x, y, picture[y][x])
print(normal, weak)
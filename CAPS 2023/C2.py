from collections import deque
for _ in range(int(input())):
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph = [tuple(map(int, input().split())) for i in range(N)]
    visited = [[False] * N for i in range(N)]
    queue = deque()
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    queue.append((y2, x2))
    visited[y2][x2] = True
    find = False
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 0 and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True
                if nx == x1 and ny == y1:
                    find = True
    if find:
        print('YES')
    else:
        print('NO')
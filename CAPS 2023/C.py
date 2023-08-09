from collections import deque
rst = []
for _ in range(int(input())):
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph = [tuple(map(int, input().split())) for i in range(N)]
    if (x1, y1) != (x2, y2):
        visited = [[False]*N for i in range(N)]
        queue = deque()
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)
        queue.append((y1 - 1, x1 - 1))
        visited[y1 - 1][x1 - 1] = True
        finded = False
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 0 and visited[ny][nx] == False:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    if (ny, nx) == (y2 - 1, x2 - 1):
                        finded = True
                        break
            if finded: break
        rst.append('YNEOS'[not finded::2])
    else:
        rst.append('YES')
print('\n'.join(rst))
'''
2
5
2 2
4 4
1 0 0 0 0
0 0 0 0 0 
0 0 0 0 0
0 0 0 0 0 
1 0 0 1 0
5
2 2
4 4
1 0 0 0 0
0 0 0 0 0 
0 0 0 1 1
0 0 1 0 0 
1 0 0 1 0
'''
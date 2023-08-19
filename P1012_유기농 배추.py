from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for testCase in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if field[y][x] == 1:
                cnt += 1
                queue = deque([(x, y)])
                while queue:
                    now = queue.popleft()
                    for i in range(4):
                        nx = now[0] + dx[i]
                        ny = now[1] + dy[i]
                        if 0 <= nx < m and 0 <= ny < n:
                            if field[ny][nx] == 1:
                                field[ny][nx] = 0
                                queue.append((nx, ny))
    print(cnt)
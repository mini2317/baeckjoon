from collections import deque
import sys
def input(): return sys.stdin.readline().strip()
n = int(input())
field = [list(input()) for i in range(n)]
cnt = 0
comCnt = []
queue = deque()
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for y in range(n):
    for x in range(n):
        if field[y][x] == "1":
            queue.append((x, y))
            comCnt.append(0)
            cnt += 1
            while queue:
                now = queue.popleft()
                field[now[1]][now[0]] = "0"
                comCnt[-1] += 1
                for i in range(4):
                    nx = now[0] + dx[i]
                    ny = now[1] + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if field[ny][nx] == "1":
                            queue.append((nx, ny))
                            field[ny][nx] = "0"
print(cnt)
for i in sorted(comCnt): print(i)
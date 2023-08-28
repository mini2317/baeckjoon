import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
n, m = map(int, input().split())
field = []
I = 3
P = 1
X = 2
O = 0
queue = deque()
for i in range(n):
    field.append([])
    temp = input()
    for j in range(m):
        if temp[j] == 'I':
            field[-1].append(I)
            queue.append((j, i))
        elif temp[j] == 'P': field[-1].append(P)
        elif temp[j] == 'X': field[-1].append(X)
        elif temp[j] == 'O': field[-1].append(O)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
cnt = 0
while queue:
    now = queue.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] <= 1:
                if field[ny][nx] == P: cnt += 1
                field[ny][nx] = X
                queue.append((nx, ny))
print(cnt if cnt else 'TT')
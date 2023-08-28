from collections import deque
n, m = map(int, input().split())
field = []
cost = []
queue = deque()
for i in range(n):
    cost.append([])
    field.append([])
    for j, num in enumerate(map(int, input().split())):
        field[-1].append(num)
        if num == 2:
            cost[-1].append(0)
            queue.append((j, i))
        else:
            cost[-1].append(-num)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
while queue:
    now = queue.popleft()
    nc = cost[now[1]][now[0]]
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1:
                if cost[ny][nx] == -1 or cost[ny][nx] > nc + 1:
                    cost[ny][nx] = nc + 1
                    queue.append((nx, ny))
            else:
                cost[ny][nx] = 0
for i in range(n):
    print(*cost[i])
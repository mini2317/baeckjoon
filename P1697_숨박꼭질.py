from collections import deque
n, k = map(int, input().split())
queue = deque([n])
time = [1000001] * 1000001
time[n] = 0
while queue:
    now = queue.popleft()
    if now > 0:
        if time[now - 1] > time[now] + 1:
            time[now - 1] = time[now] + 1
            queue.append(now - 1)
    if now < 1000000:
        if time[now + 1] > time[now] + 1:
            time[now + 1] = time[now] + 1
            queue.append(now + 1)
    if now < 500000:
        if time[now * 2] > time[now] + 1:
            time[now * 2] = time[now] + 1
            queue.append(now * 2)
print(time[k])
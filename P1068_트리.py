from collections import deque
n = int(input())
tree = [[] for i in range(n + 1)]
for i, num in enumerate(map(int, input().split())):
    tree[num].append(i)
d = int(input())
cnt = 0
queue = deque()
for i in tree[-1]:
    if i != d:
        queue.append(i)
while queue:
    now = queue.popleft()
    if tree[now]:
        added = 0
        for i in tree[now]:
            if i != d:
                queue.append(i)
                added += 1
        if added == 0: cnt += 1
    else:
        cnt += 1
print(cnt)
'''
5
-1 0 0 1 1
2
'''
from math import inf
n, m = map(int, input().split())
graph = [0] + [[] for i in range(n)]
targets = []
for i in range(n - 1):
    u, v, d = map(int, input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))
for i in range(m):
    u, v = map(int, input().split())
    targets.append((u, v))
visited = [1] + [0] * n
def dfs(idx, target):
    global visited
    visited[idx] = 1
    added = 0
    for i in graph[idx]:
        if not visited[i[0]]:
            if i[0] == target:
                return i[1]
            else:
                now = dfs(i[0], target)
                if now != inf:
                    return i[1] + now
                added += 1
    return inf
for u, v in targets:
    print(dfs(u, v))
    visited = [1] + [0] * n
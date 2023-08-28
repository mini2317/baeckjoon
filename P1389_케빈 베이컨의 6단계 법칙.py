import sys, math
sys.setrecursionlimit(10**5)
def input(): return sys.stdin.readline().strip()
n, m = map(int, input().split())
graph = {}
graphKeys = []
for i in range(m):
    a, b = map(int, input().split())
    if a in graphKeys:
        graph[a].append(b)
    else:
        graph[a] = [b]
        graphKeys.append(a)
    if b in graphKeys:
        graph[b].append(a)
    else:
        graph[b] = [a]
        graphKeys.append(b)
dist = [[math.inf] * n for i in range(n)]
def dfs(node, cnt, now):
    global dist
    if dist[now - 1][node - 1] > cnt + 1:
        dist[now - 1][node - 1] = cnt + 1
    for i in graph[node]:
        if dist[now - 1][i - 1] > cnt + 2:
            dfs(i, cnt + 1, now)
min_ = math.inf
idx = 0
for i in range(1, n + 1):
    if not i in graphKeys: continue
    dist[i - 1][i - 1] = 0
    for j in graph[i]:
        dfs(j, 0, i)
    dist[i - 1] = sum(dist[i - 1])
    if min_ > dist[i - 1]: 
        min_ = dist[i - 1]
        idx = i
print(idx)
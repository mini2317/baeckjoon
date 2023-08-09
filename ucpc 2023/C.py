import math, sys

input = sys.stdin.readline

# 거리 제곱
def distSquare(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

# 두 원이 겹치는지 확인하는 함수
def isCircleOverlap(x1, y1, r1, x2, y2, r2):
    distance = distSquare(x1, y1, x2, y2)
    if distance <= (r1 + r2) ** 2:
        return True
    else:
        return False

# 두 원을 지나는 벨트의 길이를 구하는 함수
def beltLength(x1, y1, r1, x2, y2, r2):
    br = max(r1, r2)
    sr = min(r1, r2)
    dr = br - sr
    if isCircleOverlap(x1, y1, r1, x2, y2, r2):
        return 0
    l = math.sqrt(distSquare(x1, y1, x2, y2) - dr ** 2)
    theta = math.atan(l / dr) if dr != 0 else math.pi / 2
    return 2 * l + ((math.pi - theta) * br + theta * sr) * 2

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

gearNum = int(input())
gearInfo = []
for i in range(gearNum):
    gearInfo.append(tuple(map(int, input().split())))
edges = []
for i in range(gearNum):
    for j in range(i + 1, gearNum):
        if gearInfo[i] != gearInfo[j]:
            dist = beltLength(*gearInfo[i], *gearInfo[j])
            edges.append((dist, i, j))
edges.sort()
parent = [i for i in range(gearNum)]
rank = [0] * gearNum
mst_length = 0
for edge in edges:
    length, u, v = edge
    if find(parent, u) != find(parent, v):
        mst_length += length
        union(parent, rank, u, v)
print(mst_length)

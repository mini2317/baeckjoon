import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
n, m = map(int, input().split())
field = [list(map(int, input().split())) for i in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
adj = {}
for y in range(4):
    for x in range(4 - y):
        adj[(x, y)] = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx + ny <= 3 and nx >= 0 and ny >= 0 and (nx, ny) != (0, 0):
                adj[(x, y)].append((nx, ny))

def makeTetromino(ix, iy):
    rst = 0
    visited = {}
    for y in range(4):
        for x in range(4 - y):
            visited[(x, y)] = 0
    for h in ((0, 0), (1, 0), (2, 0)):
        if ix + h[0] < 0 or n <= iy + h[1] or ix + h[0] >= m or 0 > iy + h[1]: continue
        for i in adj[h]:
            if ix + i[0] < 0 or n <= iy + i[1] or ix + i[0] >= m or 0 > iy + i[1]: continue
            for j in adj[i] + adj[h]:
                if ix + j[0] < 0 or n <= iy + j[1] or ix + j[0] >= m or 0 > iy + j[1]: continue
                if j == i or j == h: continue
                for l in adj[j] + adj[i] + adj[h]:
                    if ix + l[0] < 0 or n <= iy + l[1] or ix + l[0] >= m or 0 > iy + l[1]: continue
                    if l == i or l == j or l == h: continue
                    sum_ = field[iy + h[1]][ix + h[0]]
                    for x, y in (i, j, l): sum_ += field[iy + y][ix + x]
                    if rst < sum_: rst = sum_
    return rst

rst = 0
for y in range(n):
    for x in range(m):
        rst = max(rst, makeTetromino(x, y))
print(rst)
from collections import deque
for _ in range(int(input())):
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph = [tuple(map(int, input().split())) for i in range(N)]
    visited = [[False] * N for i in range(N)]
    queue = deque()
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
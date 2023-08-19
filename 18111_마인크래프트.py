import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
cand = 500000001
h = 0
for i in range(257):
    inventory = B
    time = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] > i:
                time += 2 * (field[y][x] - i)
            else:
                time += i - field[y][x]
            inventory += field[y][x] - i
    if cand >= time and inventory >= 0:
        cand = time
        h = i
    if cand != 500000001 and cand < time: break
print(cand, h)
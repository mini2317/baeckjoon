W, H = map(int, input().split())
world = [[0] * W for i in range(H)]
electro = [[0] * W for i in range(H)]
N = int(input())
for i in range(N):
    q = input().split()
    x = int(q[1])
    y = int(q[2])
    if q[0] == 'redstone_block':
        world[y][x] = 1
    elif q[0] == 'redstone_dust':
        world[y][x] = 2
    elif q[0] == 'redstone_lamp':
        world[y][x] = 3

while True:
    before = [[0] * W for i in range(H)]
    for y in range(H):
        for x in range(W):
            if world[y][x] == 1:
                pass
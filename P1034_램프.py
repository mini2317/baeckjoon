N, M = map(int, input().split())
save = {}
for _ in range(N):
    temp = []
    for i, t in enumerate(input()):
        if t == "0": temp.append(i)
    temp = tuple(temp)
    if temp in tuple(save):
        save[tuple(temp)] += 1
    else:
        save[tuple(temp)] = 1
K = int(input())
if K > 2 * M:
    K = K % (2 * M)
for i in range(K if K <= 2 * M else K % (2 * M)):
    p = 0
    rst = []
    while i != 0:
        if i % 2 == 0: rst.append(i)
        p += 1
        i >>= 1
    tuple(rst)
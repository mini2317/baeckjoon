a = [0] * 4
for _ in range(int(input())):
    G, C, N = map(int, input().split())
    if G == 1: a[3] += 1
    else: a[C - 2 + (C == 1)] += 1
print(*a)
N = int(input())
buildings = tuple(map(int, input().split()))
save = [0] * N
for i in range(N):
    maxCnt = 0
    for j in range(N):
        if j == i: continue
        inc = (buildings[j] - buildings[i]) / (j - i)
        cnt = 0
        if j > i:
            for x in range(i + 1, j):
                if inc * (x - i) + buildings[i] > buildings[x]:
                    cnt += 1
                else:
                    break
        else:
            for x in range(j + 1, i):
                if inc * (x - i) + buildings[i] > buildings[x]:
                    cnt += 1
                else:
                    break
        if j > i:
            for x in range(i - 1, -1, -1):
                if inc * (x - i) + buildings[i] > buildings[x]:
                    cnt += 1
                else:
                    cnt += 1
                    break
        if maxCnt < cnt : maxCnt = cnt
    save[i] += maxCnt
    print(maxCnt)
print(save)
print(max(save))
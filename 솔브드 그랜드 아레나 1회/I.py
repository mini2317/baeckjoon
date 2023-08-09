import sys
input = sys.stdin.readline
n, m = map(int, input().split())
minimum = [[0] * n, [1000001] * m]
minIdx = [[0] * n, [0] * m]
diff = [0] * (m - 1)
row, col = 0, 0
end = False
for i in range(n):
    min_1 = 1000001
    now = [*map(int, input().split())]
    for j in range(m):
        if i == 0:
            if j < m - 1:
                diff[j] = now[j + 1] - now[j]
        else:
            if j < m - 1:
                if now[j + 1] - now[j] != diff[j]:
                    end = True
        if minimum[1][j] > now[j]:
            minIdx[1][j] = i
            minimum[1][j] = now[j]
        if min_1 > now[j]:
            minIdx[0][i] = j
            min_1 = now[j]
    minimum[0][i] = min_1
    row += (min_1 == 0)
if end:
    print(-1)
else:
    temp = [[0] * n,[0] * m]
    zeroCnt = 0
    for i in range(m):
        if minimum[1][i] == 0:
            col += 1
        temp[1][i] = minimum[1][i] - minimum[0][minIdx[1][i]]
        if temp[1][i] == 0:
            zeroCnt += 1
    row += zeroCnt
    zeroCnt = 0
    for i in range(n):
        temp[0][i] = minimum[0][i] - minimum[1][minIdx[0][i]]
        if temp[0][i] == 0:
            zeroCnt += 1
    col += zeroCnt
    if col > row:
        print(n + m - col)
        temp[1] = minimum[1]
    else:
        print(n + m - row)
        temp[0] = minimum[0]
    for i in range(m):
        if temp[1][i] != 0:
            print(2, i + 1, temp[1][i])
    for i in range(n):
        if temp[0][i] != 0:
            print(1, i + 1, temp[0][i])
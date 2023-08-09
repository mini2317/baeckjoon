import sys
input = sys.stdin.readline
n, m = map(int, input().split())
diff = [0] * (n + m - 2)
end = False
point = 0
for i in range(n):
    now = [*map(int, input().split())]
    if i == 0:
        point = now[0]
        for j in range(m - 1):
            diff[j] = now[j + 1] - now[0]
    else:
        for j in range(m - 1):
            if diff[j] != now[j + 1] - now[0]:
                print(-1)
                quit()
    if n > i > 0:
        diff[m - 1 + i - 1] = now[0] - point
cnt = {}
max_ = 0
big = n + m - 2
num = -1000001
for i in range(big):
    if i < n - 1:
        if diff[i] in cnt:
            cnt[diff[i]] += 1
        else:
            cnt[diff[i]] = 1
        if cnt[diff[i]] > max_:
            max_ = cnt[diff[i]]
            num = diff[i]
    if i < m - 1:
        now = -diff[m - 1 + i]
        if now in cnt:
            cnt[now] += 1
        else:
            cnt[now] = 1
        if cnt[now] > max_:
            max_ = cnt[now]
            num = now
if point == 0:
    if max_ < 2:
        num = 0
        max_ = 2
print(n + m - max_)
for i in range(big):
    if i < n - 1:
        if point - num + diff[i] != 0:
            print(1, i + 1, point - num + diff[i])
    if i < m - 1:
        if num + diff[m - 1 + i] != 0:
            print(2, i + 1, num + diff[m - 1 + i])

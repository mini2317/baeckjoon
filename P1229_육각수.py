import sys
n = int(sys.stdin.readline())
dp = [0, 1, 2, 3, 4, 5]
hexNum = []
k = 1
while 2 * k * k - k <= n :
    hexNum.append(2 * k * k - k)
    k += 1
hexNum.append(2 * k * k - k)
for i in range(6, n + 1):
    k = 0
    min_ = 999999
    for j in hexNum:
        if j > i : break
        p = dp[i - j] + 1
        if min_ > p : min_ = p
    dp.append(min_)
print(dp[n])
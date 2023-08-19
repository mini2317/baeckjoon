a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0] * (n + 1) for _ in range(m + 1)]
max_ = 0
for i in range(1, m + 1):
    for j in range(n + 1):
        if i == 1 and j == 1:
            dp[i][j] = 0
        elif a[j - 1] == b[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_:
                max_ = dp[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(max_)
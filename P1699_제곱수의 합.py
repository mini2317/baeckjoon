n = int(input())
dp = [0] + [i for i in range(1, n + 1)]
for i in range(1, n + 1):
    f = min(dp[i - j * j] + 1 for j in range(1, int(i ** 0.5) + 1))
    dp[i] = min(dp[i], f)
print(dp[n])
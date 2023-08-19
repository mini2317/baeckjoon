dp = [0, 1, 2]
n = int(input())
for i in range(3, n + 1):
    dp.append(dp[-1] + dp[-2])
print(dp[n])
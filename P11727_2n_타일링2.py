dp = [0,1,3]
n = int(input())
for i in range(max(0, n - 2)): dp.append((dp[-1] + 2 * dp[-2]) % 10007)
print(dp[n])
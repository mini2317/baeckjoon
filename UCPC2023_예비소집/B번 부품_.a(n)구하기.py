n = int(input())
dp = [1]
start = len(dp)
for i in range(start, n + 1): dp.append((4*i-2)*dp[-1]//(i+1))
print(dp[n])
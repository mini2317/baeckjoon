dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for testCase in range(int(input())):
    n = int(input())
    if n >= len(dp):
        for i in range(n - len(dp) + 1): dp.append(dp[-1] + dp[-5])
    print(dp[n])
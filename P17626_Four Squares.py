import sys
input = sys.stdin.readline
n = int(input())
dp = []
dp2 = []
for j in range(1, int(n ** 0.5) + 1):
    dp.append(n - j * j)
    if n == j * j:
        print(1)
        quit()
for i in range(int(n ** 0.5)):
    for j in range(1, int(dp[i] ** 0.5) + 1):
        dp2.append(dp[i] - j * j)
        if dp[i] == j * j:
            print(2)
            quit()
for i in range(len(dp2)):
    for j in range(1, int(dp2[i] ** 0.5) + 1):
        if dp2[i] == j * j:
            print(3)
            quit()
print(4)
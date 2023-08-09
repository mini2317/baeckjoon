c, n = map(int, input().split())
dp = [0] + [100001] * 2000
info = {}
for _ in range(n):
    co, cu = map(int, input().split())
    if cu in tuple(info):
        info[cu] = min(info[cu], co)
    else:
        info[cu] = co
cust = tuple(info)
for i in range(1, 2001):
    for j in cust:
        if i % j == 0:
            dp[i] = min(dp[i], info[j] * (i // j), dp[i - j] + info[j])
        else:
            dp[i] = min(dp[i], dp[i - j] + info[j])
print(min(dp[c:]))
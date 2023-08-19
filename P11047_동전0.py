n, k = map(int, input().split())
coins = [int(input()) for i in range(n)][::-1]
cnt = 0
for i in coins:
    if k >= i:
        cnt += k // i
        k -= i * (k // i)
print(cnt)
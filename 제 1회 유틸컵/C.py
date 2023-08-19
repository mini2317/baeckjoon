a = sorted([int(input()) for _ in range(int(input()))], reverse = True)[:42]
cnt = 0
for i in a: cnt += (i >= 60) + (i >= 100) + (i >= 140) + (i >= 200) + (i >= 250)
print(sum(a), cnt)
X = int(input())
num = [{X}]
cnt = 0
for i in range(X):
    if 1 in num[-1]:
        print(cnt)
        break
    num.append(set())
    for j in num[-2]:
        if j % 3 == 0 : num[-1].add(j//3)
        if j % 2 == 0 : num[-1].add(j//2)
        num[-1].add(j - 1)
    cnt += 1

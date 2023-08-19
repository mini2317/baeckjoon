now = list(map(int, input().split('-')))
now[0] *= 10000
now[1] *= 100
now = sum(now)
cnt = 0
for i in range(int(input())):
    gift = list(map(int, input().split('-')))
    gift[0] *= 10000
    gift[1] *= 100
    gift = sum(gift)
    cnt += (gift >= now)
print(cnt)
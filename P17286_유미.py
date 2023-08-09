yumi = tuple(map(int, input().split()))
team = [tuple(map(int, input().split())) for _ in range(3)]
getDist = lambda x1, y1, x2, y2 : ((x1 - x2)**2 + (y1 - y2)**2)**0.5
min_ = 90
for i in range(3):
    for j in range(3):
        if j == i: continue
        for k in range(3):
            if i == k or j == k : continue
            d = getDist(*yumi, *team[i]) + getDist(*team[i], *team[j]) + getDist(*team[j], *team[k])
            if min_ > d : min_ = d
print(int(min_))
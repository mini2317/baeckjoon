import sys
s = []
save = {}
best = 0
sum_ = 0
max_ = -4001
min_ = 4001
elite = []
l = int(sys.stdin.readline().strip())
for _ in range(l):
    new = int(sys.stdin.readline().strip())
    sum_ += new
    if new < min_: min_ = new
    if new > max_: max_ = new
    find = len(s)//2
    divide = 2
    for i in range(len(s)):
        divide *= 2
        move = len(s)//divide
        if s[find] > new:
            find -= move
            if move == 0:
                find -= 1
        elif s[find] < new:
            find += move
            if move == 0:
                find += 1
        else:
            s.insert(find,new)
            break
        if move == 0:
            s.insert(find,new)
            break
    else:
        s.append(new)
    if save.get(new) is None: save[new] = 0
    save[new] += 1
    nowSave = save[new]
    if nowSave > best:
        elite = [new]
        best = nowSave
    elif nowSave == best:
        le = len(elite)
        if le == 1:
            if elite[0] > new:
                elite.append(elite[0])
                elite[0] = new
            else:
                elite.append(new)
        elif le == 2:
            if elite[0] > new:
                elite[1] = elite[0]
                elite[0] = new
            elif elite[1] > new:
                elite[1] = new
print(round(sum_/l))
print(s[l//2])
if len(elite) != 1:
    print(elite[1])
else:
    print(elite[0])
print(max_ - min_)
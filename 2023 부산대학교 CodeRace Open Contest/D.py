N,M = map(int,input().split())
time = 0
first = []
idxLi = []
scond = []
for _ in ['']*N:
    a = list(map(int,input().split()))
    min_ = min(a)
    idx = a.index(min_)
    min_2 = min(a[:idx]+a[idx:])
    first.append(min_)
    idxLi.append(idx)
    scond.append(min_2)
print(time)
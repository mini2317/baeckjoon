def brush(piece):
    i = 0
    cnt1 = 0
    cnt2 = 0
    n = len(piece)
    while i < n:
        nS = piece[i]
        while i < n:
            if nS != piece[i]:break
            i += 1
        if nS == 1 : cnt1 += 1
        else : cnt2 += 1
    return 1 + min(cnt1,cnt2)

N,M = map(int, input().split())
lastRst = 0
for _ in ['']*N:
    row = list(map(int,input().split()))
    rst = []
    i = 0
    cnt = 1
    while i < M:
        nS = row[i]
        if nS == 0:
            while i < M and nS == 0:
                i+=1
                if i >= M:break
                nS = row[i]
            cnt += 1
            if i >= M:break
        new = []
        while i < M:
            if (not row[i] in (1,2) if nS else nS != row[i]):break
            new.append(row[i])
            i += 1
        rst.append(new)
        if i >= M:break
    for piece in rst:
        lastRst += brush(piece)
print(lastRst)
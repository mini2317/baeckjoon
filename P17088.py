l = int(input())
s = sorted(map(int,input().split()))
dist = [s[i+1]-s[i] for i in range(l-1)]
if any(dist):
    if max(dist) - min(dist) <= 4:
        l2 = l-1
        d = s[-1]-s[0]
        if (d+1) % l2 == 0:d+=1
        elif (d-1) % l2 == 0:d-=1
        d//=l2
        rst1 = 0
        for i in range(1,l):
            if s[i] != s[0]+d*(i-1):rst1+=1
        rst2 = 0
        for i in range(1,l):
            if s[l-i-1] != s[-1]-d*i:rst2+=1
        print(min(rst1,rst2))
    else:
        print(-1)
else:
    print(0)
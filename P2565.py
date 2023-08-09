N=int(input())
a=dict(eval(input().replace(*' ,')) for i in ['']*N)
ra=dict((a[k],k) for k in a)
k=set(a.keys())
a=tuple(dict(sorted(a.items(),key=lambda x:x[0])).values())
rank=[{ra[a[i]]} for i in range(N)]
cnt=[1]*N
for i in range(N):
    for j in range(i):
        if cnt[j] >= cnt[i] and a[j] < a[i]:
            rank[i] = rank[j] | {ra[a[i]]}
            cnt[i] = cnt[j] + 1
m=max(cnt)
print(N-m)
for i in k-rank[cnt.index(m)]:print(i)
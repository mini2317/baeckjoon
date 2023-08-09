N=int(input())
a=list(map(int,input().split()))
cnt=[1]*N
for i in range(N):
    for j in range(i):
        if cnt[j] >= cnt[i] and a[j] < a[i]:
            cnt[i] = cnt[j]+1
print(max(cnt))
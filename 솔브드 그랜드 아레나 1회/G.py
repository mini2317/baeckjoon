input()
l=[*map(int,input().split())]
M=100001
d=[0]*M
for i in map(int,input().split()):d[i]=1
input()
for i in range(1,M):
    for j in range(i*2,M,i):
        d[j]+=d[i]
print(*[d[i]for i in l])
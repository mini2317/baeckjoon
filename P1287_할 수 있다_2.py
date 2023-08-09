n,m=map(int,input().split())
a=[*map(int,input().split())]
S=0
c=0
s=[0]
for i in range(n):
    S+=a[i]
    s.append(S)
    for j in range(i+1):
        if (s[-1]-s[j])%m==0:c+=1
print(c)
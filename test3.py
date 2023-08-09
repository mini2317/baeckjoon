N=int(input())
NN=int(input())
*A,=[list(map(int,input().split())) for i in range(NN)]
virus=[0]*(N+1)
virus[1]=1
end=1
while end:
    end=0
    for i in range(NN):
        node = A[i]
        now=node[0]
        t=node[1]
        if virus[now]*(virus[t]^1):
            end=1
            virus[t]=1
print(sum(virus)-1)
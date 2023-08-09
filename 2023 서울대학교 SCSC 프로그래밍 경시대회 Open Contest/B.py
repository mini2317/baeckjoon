N,M = map(int,input().split())
S = []
QUERY = []
for i in range(M):
    new = int(input())
    if len(QUERY) != 0 : continue
    if 2*N >= new:
        if new >= N:
            QUERY.append(new)
        else:
            for j in range(len(S)):
                if S[j] > new:
                    S.insert(j,new)
                    break
            else:
                S.append(new)

print(S)
print(len(QUERY),*QUERY)
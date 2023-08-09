N, M, K = map(int,input().split())
Q = [0]*N
def change(q):
    if len(q)==1:
        return [Q[q[0]-1] ^ Q[(q[0]+1)%N]]
    elif len(q)==2:
        return [Q[q[0]-1] ^ Q[(q[0]+1)%N],Q[q[1]-1] ^ Q[(q[1]+1)%N]]
    else:
        mid = len(q)//2
        return change(q[:mid]) + change(q[mid:])
def sum_(q):
    if len(q)==1:
        return Q[q[0]-1] ^ Q[(q[0]+1)%N]
    elif len(q)==2:
        return (Q[q[0]-1] ^ Q[(q[0]+1)%N])+(Q[q[1]-1] ^ Q[(q[1]+1)%N])
    else:
        mid = len(q)//2
        return sum_(q[:mid]) + sum_(q[mid:])
query = range(N)
for i in range(M):
    Q[int(input())] = 1
for i in range(K-1):
    Q = change(query)
print(sum_(query))
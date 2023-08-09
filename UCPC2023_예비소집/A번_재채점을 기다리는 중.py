N, K = map(int, input().split())
correct = tuple(map(int,input().split()))
check = lambda correct, query : sum(correct[i] == query[i] for i in range(N))
pull = lambda query, n : query[:n]+query[n+1:]+[-1]
push = lambda query, n : query[:n]+[-1]+query[n:-1]
query = [list(map(int,input().split()))]
max_ = check(correct, query[0])
for _ in range(K):
    next = []
    for i in range(len(query)):
        for n in range(N):
            pulled = pull(query[i],n)
            pushed = push(query[i],n)
            c1 = check(correct, pulled)
            c2 = check(correct, pushed)
            if c1 > max_: max_ = c1
            if c2 > max_: max_ = c2
            next.append(pulled)
            next.append(pushed)
    query = next[:]
print(max_)
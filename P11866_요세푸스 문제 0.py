N, K = map(int,input().split())
S = list(range(1, N + 1))
now = 0
queue = []
for i in range(N):
    temp = now
    findCnt = K
    while True:
        if S[temp%N] != -1:
            if findCnt == 1:
                break
            else:
                findCnt -= 1
        temp += 1
    now = temp
    queue.append(str(S[now%N]))
    S[now%N] = -1
print(f'<{", ".join(queue)}>')
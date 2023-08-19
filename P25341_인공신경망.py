N, M, Q = map(int, input().split())
inputWeight = [[] for _ in range(N)]
inputBias = [0] * M
for i in range(M):
    arr = list(map(int, input().split()))
    c = arr[0]
    for j in range(1, c + 1): inputWeight[arr[j] - 1].append((i, arr[c + j]))
    inputBias[i] = arr[-1]
w = list(map(int, input().split()))
hidden = [0] * M
for _ in range(Q):
    output = w[-1]
    a = list(map(int, input().split()))
    for i in range(N):
        n = a[i]
        for j in inputWeight[i]:
            hidden[j[0]] += n * j[1]
    for j in range(M):
        output += (hidden[j] + inputBias[j]) * w[j]
        hidden[j] = 0
    print(output)
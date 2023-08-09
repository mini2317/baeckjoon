A, B, N = map(int, input().split())
A %= B
for i in range(N - 1):
    A *= 10
    A %= B
print((A * 10)//B)
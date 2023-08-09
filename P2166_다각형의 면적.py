N = int(input())
p = tuple(tuple(map(int, input().split())) for i in range(N))
print(abs(sum(p[i][0] * p[(i+1)%N][1] for i in range(N)) - sum(p[(i+1)%N][0] * p[i][1] for i in range(N)))/2)
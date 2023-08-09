getSurface = lambda p, N : abs(sum(p[i][0] * p[(i+1)%N][1] - p[(i+1)%N][0] * p[i][1] for i in range(N)))/2
isInEstate = lambda p, S : sum(getSurface((S[i],S[(i+1)%3],p),3) for i in range(3)) <= getSurface(S,3)
estate = tuple(tuple(map(int, input().split())) for _ in range(3))
N = int(input())
rst = 0
for i in range(N): rst += isInEstate(tuple(map(int,input().split())), estate)
print(getSurface(estate,3),rst)
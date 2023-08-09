import sys
input = sys.stdin.readline
N,M = map(int,input().split())
S = []
sum_ = 0
for i in map(int,input().split()):
    sum_ += i
    S.append(sum_)
for _ in range(M):
    a,b=map(int,input().split())
    if a > 1:
        print(S[b-1]-S[a-2])
    else:
        print(S[b-1])
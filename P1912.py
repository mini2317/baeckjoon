N = int(input())
S = []
sum_ = 0
for i in map(int,input().split()):
    sum_ += i
    S.append(sum_)
print(max(S[i] - min(S[:i]) if i else S[i] for i in range(N)))
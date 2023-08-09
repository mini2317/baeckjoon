import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = ''.join(input().strip() for _ in range(n))
def check(a, b, n):
    sum_ = 0
    for i in range(n): sum_ += a[i] != b[i]
    return sum_
min_ = n*m+1
minPart = [] 
for y in range(n//k):
    for x in range(m//k):
        part = [a[m*(y*k+i)+x*k] for i in range(k)]
        sum_ = 0
        makeRst = [a[i][:] for i in range(n)]
        for cy in range(n//k):
            for cx in range(m//k):
                for p in range(k):
                    sum_ += check(part[p], a[cy*k+p][cx*k:(cx+1)*k], k)
                    makeRst[cy*k+p] = part[p]*(m//k)
        if sum_ < min_:
            min_ = sum_
            minPart = makeRst
print(min_)
print('\n'.join(minPart))
import math

def fastpow(a, b):
    if b == 0: return 1
    elif b == 1: return a
    h = fastpow(a, b//2)
    if b % 2 == 0:
        return h * h
    return h * h * a

N, k = map(int, input().split())
r = fastpow(10, int(math.log10(N)) + 1)
nr = N
p = 1
mod = N % k
while mod != 0:
    if p > k:
        print(-1)
        break
    nr = (nr % k) * r + N
    p += 1
    mod = nr % k
else:
    print(p)
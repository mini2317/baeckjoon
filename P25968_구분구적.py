n = int(input()) + 1
a = tuple(map(float, input().split()))
k = int(input())

def F(x):
    rst = 0
    for i in range(n): rst += a[- i - 1] * x ** (2 * i + 1) / (2 * i + 1)
    return rst

def f(x):
    rst = 0
    for i in range(n): rst += a[- i - 1] * x ** (2 * i)
    return rst

def df(x):
    rst = 0
    for i in range(1, n):
        rst += 2 * i * a[- i - 1] * (x ** (2 * i - 1))
    return rst

def solve():
    x = 0
    while df(x) == 0:
        x += 0.01
    for _ in range(200):
        x -= f(x) / df(x)
    return (-x, x) if x > 0 else (x, -x)

A, B = solve()
if k > 10000:
    print(abs(F(B) - F(A)))
else:
    dx = (B - A) / k  
    sum_ = 0
    for i in range(k // 2 + k % 2):
        sum_ += abs(f(A + i * dx + dx / 2) * dx)
    if k % 2:
        sum_ -= abs(f(A + k // 2 * dx + dx / 2) * dx) / 2
    sum_ *= 2
    print(sum_)
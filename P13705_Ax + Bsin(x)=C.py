from decimal import *
import sys
input = sys.stdin.readline
getcontext().prec = 100
A, B, C = map(Decimal, input().split())
def sin(x):
    i, s, fact, num, sign = 1, x, 1, x, 1
    for _ in range(200):
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s
pi = Decimal('3.141592653589793238462643383279502')
left = ((C / A) // pi) * pi
right = ((C / A) // pi + 1) * pi
f = lambda x : A * x + B * sin(x %(2 * pi)) < C
while right - left > 1e-20:
    mid = (left + right) / 2
    if f(mid): left = mid
    else: right = mid
print(round(mid , 6))
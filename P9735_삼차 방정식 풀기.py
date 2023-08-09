from decimal import *
getcontext().prec = 100
import sys
input = sys.stdin.readline
for testCase in range(int(input())):
    A, B, C, D = map(Decimal, input().split())
    f = lambda x : A * x ** 3 + B * x * x + C * x + D
    dfdx = lambda x : 3 * A * x * x + 2 * B * x + C
    det = B * B - 3 * A * C
    sign = A / abs(A)
    end = False
    x0 = 0
    if det < 0 :
        x0 = - B / (3 * A)
        for _ in range(200): x0 -= f(x0) / dfdx(x0)
        print(round(x0))
        end = True
    elif det == 0 :
        x0 = - B / (3 * A) + 1
        for _ in range(200): x0 -= f(x0) / dfdx(x0)
        print(round(x0))
        end = True
    else:
        alpha = (- B - Decimal.sqrt(det)) / (3 * A)
        beta = (- B + Decimal.sqrt(det)) / (3 * A)
        if sign == -1 :
            alpha, beta = beta, alpha
        dist = abs(alpha - beta)
        minimum = alpha - dist / 2 - 1
        maximum = beta + dist / 2 + 1
        for i in range(int(minimum), int(maximum) + 1):
            if f(i) == 0 :
                x0 = i
                break
    if not end:
        a, b, c = A, B + A * x0, C + B * x0 + A * x0 * x0
        g = lambda x : a * x * x + b * x + c
        d = b * b - 4 * a * c
        if d < 0:
            print(x0)
        elif d == 0:
            alpha = - b / (2 * a)
            print(*sorted(set([alpha, x0])))
        elif d > 0:
            alpha = (- b - Decimal.sqrt(d)) / (2 * a)
            beta = (- b + Decimal.sqrt(d)) / (2 * a)
            print(*sorted(set([alpha, beta, x0])))
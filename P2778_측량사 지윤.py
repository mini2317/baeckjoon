from math import gcd
from decimal import Decimal

def dist(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2).sqrt()

for t in range(int(input())):
    lines = []
    points = []
    for _ in range(3): lines.append(tuple(map(int, input().split())))
    stop = False
    for i in range(3):
        a1, b1, c1, a2, b2, c2 = lines[i//2] + lines[1 + (i > 0)]
        if a1 == 0:
            a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        if (a1 != 0 and b2 != 0) or (a2 != 0 and b1 != 0) or (a1, b1, a2, b2).count(0) < 2:
            g = gcd(a1, a2)
            n, m = a1//g, a2//g
            a2, b2, c2 = a2 * n, b2 * n, c2 * n
            a2, b2, c2 = a2 - a1 * m, b2 - b1 * m, c2 - c1 * m
            if b2 == 0:
                if a2 == 0:
                    stop = True
                    break
                x = - Decimal(c2) / a2
                y = - Decimal(c1 + a1 * x) / b1
            else:
                y = - Decimal(c2) / b2
                x = - Decimal(c1 + b1 * y) / a1
            points.append((x,y))
        else:
            stop = True
            break
    if stop:
        print('0.0000')
    else:
        a, b, c = dist(points[0], points[1]), dist(points[0], points[2]), dist(points[1], points[2])
        m = max(a, b, c)
        if m < a + b + c - m and not 0 in (a, b, c):
            print('%0.4f' % round(a * b * (1 - ((a * a + b * b - c * c)/(2 * a * b)) ** 2).sqrt() / 2, 4))
        else:
            print('0.0000')
from math import sqrt, pi
SRT = sqrt(2)
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    r0 = (a + b - sqrt(a * a + b * b)) / 2
    r = [r0] * 3
    d = [a - r0, b - r0]
    for n in range(2):
        rn = r[n]
        dn = d[n]
        c = sqrt(rn * rn + dn * dn)
        r[n] = (c * rn - rn * rn) / (c + rn)
        d[n] = dn * r[n] / rn
    r[2] *= ((SRT - 1) / (SRT + 1))
    for i in range(int(k) - 2):
        max_ = -1
        n = -1
        for j in range(3):
            if r[j] > max_:
                max_ = r[j]
                n = j
        if n == 2:
            r[2] *= ((SRT - 1) / (SRT + 1))
        else:
            rn = r[n]
            dn = d[n]
            c = sqrt(rn * rn + dn * dn)
            r[n] = (c * rn - rn * rn) / (c + rn)
            d[n] = dn * r[n] / rn
    if k == 1:
        n = r0
    else:
        n = -1
        for j in range(3):
            if r[j] > n:
                n = r[j]
    print(n * n * pi)
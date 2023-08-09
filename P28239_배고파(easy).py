from math import log2
for _ in range(int(input())):
    m = int(input())
    d = log2(m)
    s = 2 ** int(d)
    if s > m:
        d -= 1
        s = 2 ** int(d)
    if m - s == 0:
        if m == 1:
            print(0, 0)
        else:
            print(int(d) - 1, int(d) - 1)
    else:
        e = int(log2(m - s))
        c1 = s + 2 ** e
        c2 = s + 2 ** (e + 1)
        if abs(c1 - m) <= abs(c2 - m):
            print(e, int(d))
        else:
            print(e + 1, int(d))
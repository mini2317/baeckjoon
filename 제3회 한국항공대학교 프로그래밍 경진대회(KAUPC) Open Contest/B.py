a, b, c = tuple(map(int, input().split()))
d, e = tuple(map(int, input().split()))
p = (a * d * d, 2 * a * d * e + d * b, a * e * e + b * e + c)
q = (a * d, d * b, c * d + e)
D = (p[1] - q[1]) ** 2 - 4 * (p[0] - q[0]) * (p[2] - q[2])
if q[0] != p[0] :
    if D > 0:
        print("Go ahead")
    elif D == 0:
        print("Remember my character")
    else:
        print("Head on")
else:
    if p[1] == q[1] and p[2] == q[2]:
        print("Nice")
    elif p[1] == q[1] and p[2] != q[2] :
        print("Head on")
    else:
        print("Remember my character")
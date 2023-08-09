x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
def ccw (x1, y1, x2, y2, x3, y3) :
    rst = x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x1 * y3 - x2 * y1
    if rst < 0: return -1
    elif rst > 0: return 1
    return 0
c1 = ccw(x1, y1, x2, y2, x3, y3)
c2 = ccw(x1, y1, x2, y2, x4, y4)
c3 = ccw(x3, y3, x4, y4, x1, y1)
c4 = ccw(x3, y3, x4, y4, x2, y2)
print(int(c1 * c2 < 0 and c3 * c4 <= 0))
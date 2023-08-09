def ccw (x1, y1, x2, y2, x3, y3) :
    rst = x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x1 * y3 - x2 * y1
    if rst < 0: return -1
    elif rst > 0: return 1
    return 0

def crossLine(p1, p2, p3, p4):
    c1 = ccw(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
    c2 = ccw(p1[0], p1[1], p2[0], p2[1], p4[0], p4[1])
    c3 = ccw(p3[0], p3[1], p4[0], p4[1], p1[0], p1[1])
    c4 = ccw(p3[0], p3[1], p4[0], p4[1], p2[0], p2[1])
    if abs(c1) + abs(c2) == 0:
        return p1[0] <= p3[0] <= p2[0] and p1[1] <= p3[1] <= p2[1]
    return c1 * c2 < 0 and c3 * c4 <= 0

for testCase in range(int(input())):
    pos = [*map(int, input().split())]
    line = [(pos[0], pos[1]), (pos[2], pos[3])]
    top, bot = max(pos[5], pos[7]), min(pos[5], pos[7])
    left, right = min(pos[4], pos[6]), max(pos[4], pos[6])
    rect = [(left, top), (right, top), (right, bot), (left, bot)]
    for i in range(4):
        if crossLine(line[0], line[1], rect[i], rect[(i + 1) % 4]):
            print('T')
            break
    else:
        if left <= line[0][0] <= right and bot <= line[0][1] <= top and left <= line[1][0] <= right and bot <= line[1][1] <= top:
            print('T')
        else:
            print('F')
from math import acos, pi
while True:
    try:
        for _ in range(int(input())):
            sum_ = 0
            N = int(input())
            for i in range(N) :
                x1, y1, x2, y2 = map(int, input().split())
                a = x1 * x1 + y1 * y1
                b = x2 * x2 + y2 * y2
                c = (x1 - x2) ** 2 + (y1 - y2) ** 2
                sum_ += acos((a + b - c) / (2 * (a ** 0.5) * (b ** 0.5))) / (2 * pi)
            print('%.5f' % round(sum_, 5))
    except Exception:
        break
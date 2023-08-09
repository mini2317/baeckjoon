import sys, math
input = sys.stdin.readline

def getTriangleSurface(a, b, c):
    return abs((b[1] - c[1]) * a[0] + (c[1] - a[1]) * b[0] + (a[1] - b[1]) * c[0])/2

N = int(input())
total = [tuple(map(int, input().split())) for _ in range(N)]
max_ = 0
if N == 3:
    print(getTriangleSurface(total[0], total[1], total[2]))
else:
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                s = getTriangleSurface(total[i], total[j], total[k])
                if max_ < s: max_ = s
    print(max_)
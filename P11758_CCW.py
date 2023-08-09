p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))
rst = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1] - p2[0] * p1[1]
print(abs(rst)//rst if rst != 0 else 0)
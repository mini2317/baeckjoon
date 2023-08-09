n = int(input())
rst = []
for i in range(n):
    a = tuple(map(int, input().split()))
    b = sorted(a[2:])
    rst.append(max(a[0],a[1]) + b[-1] + b[-2])
print(max(*rst))
from math import lcm
a = tuple(map(int, input().split()))
min_ = 1000000
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            if (l := lcm(a[i],a[j],a[k])) < min_: min_ = l
print(min_)
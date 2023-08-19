import math
n = int(input())
m = int(input())
b = list(range(10))
if m == 10:
    input()
    print(abs(n - 100))
    quit()
if m == 0:
    length = int(math.log10(n)) + 1 if n else 1
    print(min(length, abs(n - 100)))
    quit()
for i, num in enumerate(map(int, input().split())):
    left = 0
    right = 9 - i
    while left <= right:
        mid = (left + right) // 2
        if b[mid] > num: right = mid - 1
        else: left = mid + 1
    b.pop(right)
def getter(nowNum, level):
    nowNumLen = int(math.log10(nowNum)) + 1 if nowNum else 1
    dist = min(abs(n - nowNum) + nowNumLen, abs(n - 100))
    if level == 1: return dist
    if level == 8: return min(getter(nowNum * 10 + b[i], level - 1) for i in range(10 - m))
    return min(min(getter(nowNum * 10 + b[i], level - 1) for i in range(10 - m)), dist)
print(getter(0, 8))
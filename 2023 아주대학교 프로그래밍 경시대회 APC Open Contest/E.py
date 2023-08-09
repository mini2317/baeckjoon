def search(a, d, x):
    left = 1
    right = 1000000
    while left <= right:
        mid = (left + right) // 2
        f = int(d * (mid * mid - mid) // 2 + mid + a)
        if f == x: return mid, 1
        if f < x: left = mid + 1
        else: right = mid - 1
    return right + 1, x - int(d * (right * right - right) // 2 + right + a) + 1
for _ in '.'*int(input()):print(*search(*map(int, input().split())))
while (n := int(input())) != 0:
    left = 1
    right = 50
    mid = 25
    rst = []
    while left + 1 < right:
        mid = (left + right) // 2
        if mid < n : left = mid + 1
        elif mid > n : right = mid - 1
        else : break
        rst.append(mid)
    rst.append(n)
    print(*rst)
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
left = 0
right = 2147483648
arr = [int(input()) for i in range(K)]
while left <= right:
    mid = (left + right) // 2
    sum_ = 0
    for i in arr: sum_ += i // mid
    if sum_ < N: right = mid - 1
    else: left = mid + 1
print(right)
'''
3 4
2
6
19
'''
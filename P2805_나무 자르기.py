n, m = map(int, input().split())
trees = list(map(int, input().split()))
def check(trees, cut):
    cnt = 0
    for i in trees:
        if i > cut:
           cnt += i - cut
    return cnt
left = 0
right = max(trees)
while left <= right:
    mid = (left + right) // 2
    if check(trees, mid) < m: right = mid - 1
    else: left = mid + 1
print(right)
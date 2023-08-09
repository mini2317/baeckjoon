n, k = map(int, input().split())
people = tuple(map(int, input().split()))
diff = [max(abs(people[i + 1] - people[i]) if i < n - 1 else 0 , abs(people[i - 1] - people[i]) if i > 0 else 0) for i in range(n)]
maxDiff = max(diff) + 1
result = 1_000_000_000
def check(score):
    tired = 0
    for i in range(n): tired += diff[i] > score
    return tired > k
start, end = 0, maxDiff
while start < end:
    mid = (start + end) / 2
    if check(mid): start = mid + 1
    else: end = mid
print(int(end))
'''
5 3
1 5 2 4 3
'''
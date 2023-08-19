import sys
def input(): return sys.stdin.readline().strip()
n = int(input())
timeZone = []
for i in range(n):
    s, e = map(int, input().split())
    if i == 0:
        timeZone.append((s, e))
        continue
    left = 0
    right = i
    while left <= right and left + right < 2 * i:
        mid = (left + right) // 2
        #print(timeZone,mid)
        if timeZone[mid][0] < s: left = mid + 1
        else: right = mid - 1
    timeZone.insert(left, (s, e))
print(timeZone)
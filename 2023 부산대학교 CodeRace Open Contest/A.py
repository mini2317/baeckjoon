N = int(input())
heights = list(map(int, input().split()))
maxNum = heights[0]
cnt = 1
i = 0
while i < N:
    i += 1
    if i > N-1:
        break
    while maxNum > heights[i]:
        maxNum = heights[i]
        i += 1
        if i > N-1:
            break
    if i > N-1:
        break
    maxNum = heights[i]
    cnt += 1
if maxNum < heights[-1]:
    cnt += 1
print(cnt)
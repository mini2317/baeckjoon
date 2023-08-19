n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rank = []
for i in range(n):
    rank.append(1)
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[-1] += 1
print(*rank)
input()
numbers = tuple(map(int,input().split()))
cnt = 0
preNum = 0
for number in numbers:
    if preNum >= number:cnt += 1
    preNum = number
if preNum >= numbers[0]: cnt += 1
print(cnt)
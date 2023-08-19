import sys
input = sys.stdin.readline
from collections import deque
queue = deque()
dx = sum([[[0] * i + [-1] + [0] * (11 - i), [0] * i + [1] + [0] * (11 - i)] for i in range(11)], start= [])
def getTomatoes(size, pos):
    global queue
    if len(size) > 1: return [getTomatoes(size[1:], pos + [i]) for i in range(size[0])]
    else:
        line = list(map(int, input().split()))
        for i in range(size[0]):
            if line[i] == 1: queue.append(pos + [i])
        return line
size = list(map(int, input().split()))[::-1]
field = getTomatoes(size, [])
max_ = 0
while queue:
    now = queue.popleft()
    item = field[now[0]][now[1]][now[2]][now[3]][now[4]][now[5]][now[6]][now[7]][now[8]][now[9]][now[10]]
    if max_ < item : max_ = item
    for i in range(22):
        temp = []
        for j in range(11):
            temp.append(now[j] + dx[i][j])
            if not (0 <= now[j] + dx[i][j] < size[j]):
                break
        else:
            if field[temp[0]][temp[1]][temp[2]][temp[3]][temp[4]][temp[5]][temp[6]][temp[7]][temp[8]][temp[9]][temp[10]] == 0:
                field[temp[0]][temp[1]][temp[2]][temp[3]][temp[4]][temp[5]][temp[6]][temp[7]][temp[8]][temp[9]][temp[10]] = item + 1
                queue.append(temp)
def searchZero(field, size):
    if len(size) > 1:
        for i in range(size[0]): searchZero(field[i], size[1:])
    else:
        if 0 in field:
            print(-1)
            quit()
searchZero(field, size)
print(max_ - 1)
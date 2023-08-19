from collections import deque
import sys
input = sys.stdin.readline
START = ['Start']
ISLAND = ['Island']
GET = ['Get']
SPACE = ['Space']
def inputLine(n):
    cnt = 0
    line = []
    for i in range(n - 2):
        now = input().split()
        if now[0] == 'G':
            line.append('G')
        else:
            line.append(('L', int(now[1])))
            cnt += 1
    return line, cnt

def arrive(pre, now, money, city, n, w, green, stun, goldenKey):
    nowSquare = now % (4 * n - 4)
    #print(nowSquare, lines[nowSquare])
    if nowSquare < pre % (4 * n - 4):
        #print('wage :', w)
        money += w
    if lines[nowSquare][0] == 'L' and not nowSquare in city:
        if money >= lines[nowSquare][1]:
            money -= lines[nowSquare][1]
            city.append(nowSquare)
    elif lines[nowSquare][0] == 'G':
        q, v = goldenKey.popleft()
        goldenKey.append((q, v))
        if q == 1:
            money += v
        elif q == 2:
            money -= v
            if money < 0:
                print('LOSE')
                quit()
        elif q == 3:
            green += v
            money -= v
            if money < 0:
                print('LOSE')
                quit()
        elif q == 4:
            pre, now, money, city, green, stun, goldenKey = arrive(now, now + v, money, city, n, w, green, stun, goldenKey)
    elif lines[nowSquare][0] == SPACE:
        pre, now, money, city, green, stun, goldenKey = arrive(now, 0, money, city, n, w, green, stun, goldenKey)
    elif lines[nowSquare][0] == GET:
        money += green
        green = 0
    elif lines[nowSquare][0] == ISLAND:
        stun = 3
    return pre, now, money, city, green, stun, goldenKey

def rollTheDice():
    dice1, dice2 = map(int, input().split())
    return dice1 + dice2, dice1 == dice2

n, s, w, g = map(int, input().split())
green = 0
stun = 0
goldenKey = deque()
for i in range(g):
    q, v = map(int, input().split())
    goldenKey.append((q, v))
cityCnt = 0
lines = [START]
line, cnt = inputLine(n)
lines += line
cityCnt += cnt
lines.append(ISLAND)
line, cnt = inputLine(n)
lines += line
cityCnt += cnt
lines.append(GET)
line, cnt = inputLine(n)
lines += line
cityCnt += cnt
lines.append(SPACE)
line, cnt = inputLine(n)
lines += line
cityCnt += cnt
now = 0
money = s
city = []
for i in range(int(input())):
    pre = now
    dice, isDouble = rollTheDice()
    if stun:
        if isDouble:
            stun = 0
        else:
            stun -= 1
    else:
        now += dice
        pre, now, money, city, green, stun, goldenKey = arrive(pre, now, money, city, n, w, green, stun, goldenKey)
if len(city) == cityCnt:
    print('WIN')
else:
    print('LOSE')
#print(len(city), cityCnt)
'''
6 20000 10000 4
1 2000
4 1
2 3000
3 5000
L 500
L 1000
L 1500
G
L 1000
L 2000
G
L 3000
L 2000
G
L 4000
L 6000
G
L 3000
L 6000
L 9000
18
1 1
3 1
3 2
3 3
1 1
1 1
1 2
2 1
6 5
6 6
3 1
5 4
1 1
2 3
6 3
5 5
2 1
1 3
'''
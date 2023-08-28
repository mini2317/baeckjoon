from collections import deque
import sys
def input(): return sys.stdin.readline().strip()
n, m = map(int, input().split())
move = {}
moveKeys = []
minimum = [1000000] * 101
minimum[1] = 0
for i in range(n + m):
    u, v = map(int, input().split())
    move[u] = v
    moveKeys.append(u)
onGoal = []
queue = deque([1])
while queue:
    now = queue.popleft()
    cnt = minimum[now]
    for i in range(1, 7):
        dice = now + i
        if dice > 100: continue
        if dice in moveKeys:
            if minimum[move[dice]] > cnt + 1:
                minimum[move[dice]] = cnt + 1
                queue.append(move[dice])
        else:
            if minimum[dice] > cnt + 1:
                minimum[dice] = cnt + 1
                queue.append(dice)
print(minimum[100])
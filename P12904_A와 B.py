from collections import deque
S = input()
T = input()
n, m = len(S), len(T)
save = deque([T])
end = False
while True:
    if len(save[0]) <= n: break
    a = save.popleft()
    if a[-1] == 'A':
        if a[:-1] == S:
            print(1)
            end = True
            break
        if not a[:-1] in save:
            save.append(a[:-1])
    else:
        if a[:-1][::-1] == S:
            print(1)
            end = True
            break
        if not a[:-1][::-1] in save:
            save.append(a[:-1][::-1])
if not end: print(0)
from collections import deque
for testCase in range(int(input())):
    N, M = map(int, input().split())
    queue = deque(((n, int(i)) for n,i in enumerate(input().split())))
    cnt = 0
    end = False
    while queue:
        temp = deque()
        for i in range(len(queue)):
            max_ = max(list(queue) + list(temp), key = lambda x : x[1])[1]
            now = queue.popleft()
            if max_ == now[1]:
                cnt += 1
                if now[0] == M:
                    end = True
                    break
            else: temp.append(now)
        if end: break
        queue = temp
    print(cnt)
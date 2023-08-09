arr = []
first = ''
last = ''
for i in range(int(input())):
    now = input()
    if now == '?':
        if len(arr) != 0:
            first = arr[-1][-1]
    else:
        if len(arr) != 0:
            if arr[-1] == '?':
                last = now[0]
    arr.append(now)
for _ in range(int(input())):
    now = input()
    f = (now[0] == first if first != '' else True)
    l = (now[-1] == last if last != '' else True)
    if f and l and (not now in arr):
        print(now)
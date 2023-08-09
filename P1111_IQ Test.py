n = int(input())
arr = [*map(int, input().split())]
if n == 1:
    print('A')
elif n == 2:
    if arr[1] == arr[0]: print(arr[1])
    else: print('A')
else:
    A = 0
    if (arr[1] - arr[0]): A = (arr[2] - arr[1]) // (arr[1] - arr[0])
    now = arr[0]
    dn = arr[1] - arr[0]
    for i in range(n):
        if now != arr[i]:
            print('B')
            break
        now += dn
        dn *= A
    else:
        print(now)
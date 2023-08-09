def fastMul(arr,a):
    mid = len(arr)//2
    match len(arr):
        case 1: return [arr[0]*a]
        case 2: return [arr[0]*a,arr[1]*a]
        case _: return fastMul(arr[:mid],a)+fastMul(arr[mid:],a)
for a in range(1,10001):
    c = a
    dp = [int(str(a)[i]) for i in len(str(a))]
    for b in range(0,10000):
        c *= a
        dp = fastMul(dp,b)
    print(a)
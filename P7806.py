while True:
    try:
        n,k = map(int,input().split())
        if n >= k:print(k)
        elif n in (0,1) : print(1)
        else:
            soinsu = {}
            divided = k
            for i in range(2,int(k ** 0.5) + 1):
                while divided%i == 0:
                    if soinsu.get(i) is None:
                        soinsu[i] = 1
                    else:
                        soinsu[i] += 1
                    divided //= i
            if divided != 1:
                soinsu[divided] = 1
            rst = 1
            for i in tuple(soinsu):
                num = i
                cnt = 0
                while num <= n:
                    cnt += n // num
                    num *= i
                rst *= i**min(cnt+n//i,soinsu[i])
            print(rst)
    except:
        exit()
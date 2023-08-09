sum_ = lambda x : (x**2+x)//2
n = 0
q = int(input()) - 1
if q == 0 : print(1)
else:
    while True:
        if 6*sum_(n) < q and q <= 6*sum_(n+1):
            break
        n += 1
    print(n+2)
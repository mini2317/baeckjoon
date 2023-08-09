def fastPow(a,b,c):
    if b == 0:
        return 0
    elif b == 1:
        return a%c
    else:
        return (fastPow(a,b//2,c)**2*(a if b % 2 else 1))%c
    
tsc = int(input())
for i in [0]*tsc:
    a,b = map(int,input().split())
    rst = fastPow(a,b,10)
    print(rst if rst else 10)
def ppow(a,b,c):
    if b == 0:
        return 0
    elif b == 1:
        return a%c
    else:
        return (ppow(a,b//2,c)**2*(a if b % 2 else 1))%c
print(ppow(*map(int,input().split())))
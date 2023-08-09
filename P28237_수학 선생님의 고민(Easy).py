def find(n):
    for a in range(1,n+1):
        if n % a != 0:
            continue
        c = n // a
        b = n+1-(5*n*n + 10*n + 1)**0.5
        d = n+1+(5*n*n + 10*n + 1)**0.5
        if b % (2*c) == 0 and d % (2*a) == 0:
            return (a,int(b//(2*c)),c,int(d//(2*a)))
n = int(input())
rst = find(n)
if rst is not None :
    print(*rst)
else:
    print(-1)
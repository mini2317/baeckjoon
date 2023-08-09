sigma = lambda x:(x**2+x)//2
def rs(x,c):
    a=x
    for i in range(c):a=sigma(a)
    return a
for tc in range(int(input())):
    k=int(input())
    n=int(input())
    for j in (rs(i,n-i) for i in range(n+1,1,-1)):
        print(j)
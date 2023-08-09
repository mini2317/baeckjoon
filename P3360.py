n=int(input())
a=n//3
print(((n*a+n-3*(a**2+a)//2-n%2-n//6)//2+a+1)%10**6)
n=int(input());print(int((n*(n//3+1)-3*((n//3)**2+(n//3))//2-(n%2)-(n//6))//2+n//3+1)%1000000)
print(((sum((n-3*i)//2+1 for i in range(n//3+1)))%1000000))

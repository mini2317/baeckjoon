memo = [1,1]
def factorial(n):
    if n <= len(memo) - 1: return memo[n]
    elif n == len(memo):
        memo.append(memo[-1]*n)
    else:
        memo.append(factorial(n-1)*n)
    return memo[-1]
for _ in '.'*int(input()):
    N,R = map(int,input().split())
    print(factorial(R)//(factorial(N)*factorial(R-N)))
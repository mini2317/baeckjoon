PRIME_NUM = (2,3,5,7,11,13,17)
REMAINDER = (1,4,6,8,9,10,12,14,15,16,18)
aPercent = int(input())/100
bPercent = int(input())/100
def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1

def P(n,r):
    return factorial(n)/factorial(n-r)

a = [aPercent**score + (1-aPercent)**(18-score) for score in range(1,19)]
b = [bPercent**score + (1-bPercent)**(18-score) for score in range(1,19)]
print(a,b)
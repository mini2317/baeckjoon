import math
n = int(input())
print(2**math.ceil(math.log(n,2))-2*(2**math.ceil(math.log(n,2))-n))
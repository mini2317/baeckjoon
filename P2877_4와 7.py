import math;n=int(input());l=int(math.log2(n+1));a=bin(n-(2**l-1))[2:].replace('0','4').replace('1','7');print('4'*(l-len(a))+a)
from math import gcd
def roll(n):
    mid = len(n)//2
    match len(n):
        case 1:
            return n[0]
        case 2:
            return n[0]+n[1]
    return max(roll(n[:mid]) + gcd(*n[mid:]), roll(n[mid:]) + gcd(*n[:mid]))
N = int(input())
S = list(map(int,input().split()))
mid = N//2
print(max(roll(S[:mid]) + gcd(*S[mid:]), roll(S[mid:]) + gcd(*S[:mid])) if N != 1 else S[0])
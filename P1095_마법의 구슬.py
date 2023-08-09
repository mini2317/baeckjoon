import math
S, F, M = map(int, input().split())
R = math.comb(S + F, F)
if M <= R:
    if M != 1:
        prime = {}
        era = [False] * 2 + [True] * M
        for i in range(2, M):
            if era[i]:
                p = i
                while p <= M:
                    era[p] = False
                    p += i
                if R % i == 0 :
                    prime[i] = 0
                    while R % i == 0:
                        prime[i] += 1
                        R //= i
        print(R)
        print(prime)
        if prime:
            print(prime)
        else:
            print(1)
    else:
        print(-1)
else:
    print(R)
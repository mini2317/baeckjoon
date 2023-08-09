P = 1000000007
N, a = map(int, input().split())
def fastpow(a, b):
    if b == 0: return 1
    elif b == 1: return a
    h = fastpow(a, b//2)
    if b % 2 == 0:
        return h * h % P
    return h * h * a % P

print(int((N - 1) * ((fastpow(N, a + 1) - fastpow(N - 1, a + 1) + fastpow(N - 1, a - 1))))%P)
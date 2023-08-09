for _ in range(int(input())):
    a,b,c, = sorted(map(int, input().split()))
    print('YNEOS'[c >= a+b::2])
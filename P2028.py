for _ in range(int(input())):
    a = input()
    print('YNEOS'[str(int(a) ** 2)[-len(a):]!=a::2])
for i in range(int(input())):
    a = input()
    mid = len(a)//2
    print('YNEOS'[a[:mid] == a[len(a)-mid::-1]::2])
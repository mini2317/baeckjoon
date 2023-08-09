while 1:
    a=input()
    if a=="0":break
    print('yneos'[a[:len(a)//2]!=a[len(a)//2+(len(a)%2):][::-1]::2])
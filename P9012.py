for _ in '.'*int(input()):
    query = input()
    level = 0
    for i in query:
        if i == '(': level += 1
        else: level -= 1
        if level < 0:break
    print('YNEOS'[level!=0::2])
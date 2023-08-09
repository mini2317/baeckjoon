from math import ceil
chart = {"@":"a", "[":"c", "!":"i", ";":"j", "^":"n", "0":"o", "7":"t", "\\\\'":"w","\\'":"v"}
for _ in '.'*int(input()):
    test = input()
    change = test
    cnt = 0
    stop = False
    for char in tuple(chart):
        change = change.replace(char,chart[char])
        cnt += test.count(char)
        stop = cnt >= ceil(len(test)/2)
        if stop:
            print("I don't understand")
            break
    if not stop:
        print(change)
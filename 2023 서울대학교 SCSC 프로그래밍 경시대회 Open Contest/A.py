from math import floor
operator = ["/","*","+","-"]
s = input()
num1 = ""
oper = ""
num2 = ""
for i,char in enumerate(s):
    if char in operator:
        if char == "-" and num1 == "":
            num1 += "-"
        else:
            oper = char
            num2 = s[i+1:]
            break
    else:
        num1 += char
num1 = int(num1,8)
num2 = int(num2,8)
if oper == "/" and num2 == 0:
    print('invalid')
else:
    cal = oct(floor(eval(f'({num1}){oper}({num2})')))
    if cal[0] == "-":
        print("-"+cal[3:])
    else:
        print(cal[2:])
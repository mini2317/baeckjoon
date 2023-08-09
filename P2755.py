import math
grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
total = 0
gradeSum = 0
for _ in range(int(input())):
    inp = input().split()
    total += int(inp[1])
    gradeSum += int(inp[1]) * grade[inp[2]]
rst = round(gradeSum/total+0.0000001,2)
print(f'{int(rst)}.{str(round(rst-int(rst),2))[2:].ljust(2,"0")}')
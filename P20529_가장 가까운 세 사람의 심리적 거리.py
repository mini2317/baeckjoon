import sys
def input(): return sys.stdin.readline().strip()
combs = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
for testCase in range(int(input())):
    n = int(input())
    if n > 32:
        input()
        print(0)
        continue
    people = input().split()
    temp = []
    for i, c1 in enumerate(people):
        for j, c2 in enumerate(people[i + 1:]):
            for c3 in people[i + j + 2:]:
                cnt = 0
                for l in range(4):
                    cnt += (c1[l] != c2[l]) + (c2[l] != c3[l]) + (c1[l] != c3[l])
                temp.append(cnt)
    print(min(temp))
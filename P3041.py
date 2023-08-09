correct = list('ABCDEFGHIJKLMNO.')
query = sum([list(input()) for i in range(4)],[])
dist = 0
for i in range(len(correct)):
    alphabet = correct[i]
    if alphabet != '.':
        x = query.index(alphabet) % 4
        y = query.index(alphabet) // 4
        dist += abs(x - i % 4) + abs(y - i // 4)
print(dist)
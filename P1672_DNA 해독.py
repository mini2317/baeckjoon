from collections import deque
n = int(input())
dna = input()
alphabet = {
    'A' : 0,
    'G' : 1,
    'C' : 2,
    'T' : 3
}
chart = [[0, 2, 0, 1], [2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 1, 3]]
dna = deque(alphabet[dna[i]] for i in range(n))
for i in range(n - 1):
    an = dna.pop()
    an_1 = dna.pop()
    dna.append(chart[an_1][an])
print('AGCT'[dna[0]])
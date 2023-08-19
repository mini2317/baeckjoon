n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
class Pair:
    def __init__(self, w, b) -> None:
        self.w = w
        self.b = b
    def __add__(self, other):
        return Pair(self.w + other.w, self.b + other.b)
    def __str__(self):
        return f'{self.w}\n{self.b}'
def cutPaper(pos, size):
    if all(all(paper[pos[1] + y][pos[0] : pos[0] + size]) for y in range(size)):
        return Pair(0, 1)
    if all(not any(paper[pos[1] + y][pos[0] : pos[0] + size]) for y in range(size)):
        return Pair(1, 0)
    return cutPaper(pos, size // 2) + cutPaper((pos[0], pos[1] + size // 2), size // 2) + cutPaper((pos[0] + size // 2, pos[1]), size // 2) + cutPaper((pos[0] + size // 2, pos[1] + size // 2), size // 2)
print(cutPaper((0, 0), n))
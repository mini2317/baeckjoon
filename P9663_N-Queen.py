n = int(input())
def setBoard():
    global board, queens
    board = [[0] * n for _ in range(n)]
    queens = []

def placeQueen(x, y):
    global board
    if board[y][x] == 0:
        board[y][x] = 1
        for i in range(1, n):
            if x + i >= n: break
            board[y][x + i] = 1
        for i in range(1, n):
            if x - i < 0: break
            board[y][x - i] = 1
        for i in range(1, n):
            if y + i >= n: break
            board[y + i][x] = 1
        for i in range(1, n):
            if x - i < 0: break
            board[y - i][x] = 1
        for i in range(1, n):
            if x + i >= n or y + i >= n: break
            board[y + i][x + i] = 1
        for i in range(1, n):
            if x + i >= n or y - i < 0: break
            board[y - i][x + i] = 1
        for i in range(1, n):
            if x - i < 0 or y + i >= n: break
            board[y + i][x - i] = 1
        for i in range(1, n):
            if x - i < 0 or y - i < 0: break
            board[y - i][x - i] = 1
    
queenSet = []
for y in range(n):
    for x in range(n):
        setBoard()
        queens.append(placeQueen(x, y))
        for y1 in range(n):
            for x1 in range(n):
                now = placeQueen(x1, y1)
                if now is not None:
                    queens.append(now)
        if not queens in queenSet or 1:
            queenSet.append(queens[:])
print(queenSet)
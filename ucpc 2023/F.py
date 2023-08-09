import sys
input = sys.stdin.readline
def update_pattern(pattern, grid):
    N = len(grid)
    
    if pattern == 'RO':
        for i in range(0,N,2):
            temp = grid[i].pop()
            grid[i].insert(0,temp)
    elif pattern == 'RE':
        for i in range(1,N,2):
            temp = grid[i].pop()
            grid[i].insert(0,temp)
    elif pattern == 'CO':
        for j in range(0,N,2):
            temp = grid[-1][j]
            for i in range(N-1, 0, -1):
                grid[i][j] = grid[i-1][j]
            grid[0][j] = temp
    elif pattern == 'CE':
        for j in range(1,N,2):
            temp = grid[-1][j]
            for i in range(N-1, 0, -1):
                grid[i][j] = grid[i-1][j]
            grid[0][j] = temp
    elif pattern.startswith('S'):
        _, r1, c1, r2, c2 = pattern.split()
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
        grid[r1-1][c1-1], grid[r2-1][c2-1] = grid[r2-1][c2-1], grid[r1-1][c1-1]
    
    return grid

def final_state(N, Q, patterns):
    grid = [[(i*N) + j + 1 for j in range(N)] for i in range(N)]
    
    for pattern in patterns:
        grid = update_pattern(pattern, grid)
    
    return grid

N, Q = map(int,input().split())
patterns = []
for i in range(Q):
  patterns.append(input().strip())

result = final_state(N, Q, patterns)
for row in result:
    print(*row)
move = {
    'U':0,
    'R':0,
    'X':0
}
cnt = 0
input()
for newMove in input():move[newMove]+=1
for _ in '.'*int(input()):
    x,y = map(lambda x : int(x)-1,input().split())
    X = min(min(x,y),move['X'])
    x -= X
    y -= X
    UR = min(move['U'],move['R'])
    X = min(min(x,y),UR)
    x -= X
    y -= X
    U = move['U'] - X
    R = move['R'] - X
    x = max(0,x - R)
    y = max(0,y - U)
    if not any((x,y)): cnt+=1
print(cnt)
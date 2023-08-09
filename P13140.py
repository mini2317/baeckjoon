target = int(input())
hello = []
world = []
token = {
    0 : ((0,0),(5,5)),
    1 : ((0,1),(2,9)),
    2 : ((1,1),(3,9)),
    3 : ((1,2),(4,9)),
    4 : ((1,3),(5,9)),
    5 : ((1,4),(6,9)),
    6 : ((1,5),(7,9)),
    7 : ((1,6),(8,9)),
    8 : ((1,7),(9,9)),
    9 : ((1,8))
}
targetNum = [target%(10**(i+1))//(10**i) for i in range(6)][::-1]
if target > 199998 or target < 20000 or (targetNum[-1] == 9 and targetNum[-2]%2 == 1):
    print('No Answer')
else:
    for o in range(10):
        for d in range(10):
            pass
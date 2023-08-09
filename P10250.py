for _ in '.'*int(input()):
    H,W,N = map(int,input().split())
    n = N-1
    print(str(n%H+1)+str(n//H+1).rjust(2,"0"))
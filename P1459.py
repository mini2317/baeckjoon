X,Y,W,S=map(int,input().split());print((abs(X-Y)*W+min(X,Y)*S if W<S else(abs(X-Y)%2)*W+(abs(X-Y)//2)*2*S+min(X,Y)*S) if W*2>S else W*(X+Y))
from collections import deque
from sys import stdin
input = stdin.readline

H, W = map(int,input().split())
graph = [[0]*W for _ in range(H)]
for y in range(H):
    row = map(int,input().split())
    
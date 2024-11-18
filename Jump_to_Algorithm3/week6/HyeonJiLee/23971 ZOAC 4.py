from math import ceil
H,W,N,M = map(int,input().split())
print(ceil(H/(N+1)) * ceil(W/(M+1)))
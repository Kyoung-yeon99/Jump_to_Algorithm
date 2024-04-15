# 여행 계획에 속한 도시들을 순서대로 갈 수 있는지 판별
import sys

input = sys.stdin.readline
N = int(input()) # 도시의 수
M = int(input()) # 여행할 도시들의 수
matrix = [] # 인접 행렬
for i in range(N): # 도로 여부
    info = list(map(int, input().split()))
    matrix.append(info)

plan = list(map(int, input().split())) # 여행 계획
parent = [i for i in range(N)]

def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for i in range(N-1):
    for j in range(i+1, N):
        if matrix[i][j] == 1:
            union(parent, i, j)

possible = True # 계획 가능 여부
for i in range(M-1): # 방문하려는 도시에 대해
    if find(parent, plan[i]-1) != find(parent, plan[i+1]-1):
        possible = False
        break

print('YES') if possible else print('NO')

    
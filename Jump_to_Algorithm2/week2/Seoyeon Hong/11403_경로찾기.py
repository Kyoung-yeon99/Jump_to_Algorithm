# 가중치 없는 방향 그래프 G가 주어졌을 때, 
# 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 정점의 개수
l = [set() for _ in range(N)] # 인접 리스트
path = [[0 for _ in range(N)] for _ in range(N)] # 경로 유무 체크

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            l[i].add(j)

for sv in range(N): # 각 정점에 대해
    q = deque()
    for av in l[sv]: # 정점과 인접한 정점을 큐에 추가
        path[sv][av] = 1
        q.append(av)
    while q: # 연결된 모든 정점을 확인할 때 까지 반복
        cv = q.pop()
        l[sv].add(cv)
        path[sv][cv] = 1
        for nv in l[cv]:
            if nv == sv: # 자기 자신으로 연결될 경우
                l[sv].add(nv)
                path[sv][sv] = 1
            elif nv not in l[sv]:
                path[cv][nv] = 1
                q.append(nv)

for row in path:
    print(*row)
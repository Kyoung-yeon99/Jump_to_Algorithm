# 두 정점 사이의 거리의 최댓값
import sys
from collections import deque

input = sys.stdin.readline
V = int(input()) # 정점의 개수
adj = [[] for _ in range(V+1)] # 인접 리스트

for i in range(1, V+1):
    info = list(map(int, input().split()))
    node = info[0] # 정점 번호
    info = info[1:-1]
    for j in range(len(info)//2):
        adj[node].append((info[2*j], info[2*j+1]))

def find_farthest_node(start): # 가장 먼 정점과 해당 정점까지의 거리 반환
    farthest_node, max_distance = start, 0
    visited = [False] * (V+1)
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        v, d = q.popleft()
        if d > max_distance:
            farthest_node, max_distance = v, d
        for nv, nd in adj[v]:
            if not visited[nv]:
                q.append((nv, d+nd))
                visited[nv] = True
 
    return farthest_node, max_distance

a, _ = find_farthest_node(1) # 임의의 점인 1번 점에서 가장 먼 정점 찾기
b, d = find_farthest_node(a) # 점 a에서 가장 먼 점까지의 거리 == 트리의 지름
print(d)

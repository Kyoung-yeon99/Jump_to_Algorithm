# 최소 스패닝 트리: 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 크루스칼 알고리즘
import sys

input = sys.stdin.readline
V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
parent = [0] * (V + 1)
edges = [] # 인접리스트
weights = 0

for _ in range(E):
    A, B, C = map(int, input().split()) # C: 간선의 가중치, 음수 가능
    edges.append((C, A, B))

edges.sort()

# 부모를 자기 자신으로 초기화
for i in range(1, V+1):
    parent[i] = i

# 원소 x가 속한 집합 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 간선 연결
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않을 경우 집합에 포함
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        weights += cost

print(weights)
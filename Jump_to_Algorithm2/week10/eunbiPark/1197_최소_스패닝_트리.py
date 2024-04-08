# 스패닝 트리 - 모든 정점이 연결되어 있으며 사이클이 없는 트리
# kruskal 알고리즘 사용
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []

for _ in range(e):
    edges.append(list(map(int, input().split())))

root = dict()
for i in range(1, v + 1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x

edges.sort(key= lambda x : x[2])
total = 0

for e in edges:
    if find(e[0]) == find(e[1]):
        continue
    else:
        total += e[2]
        union(e[0], e[1])

print(total)
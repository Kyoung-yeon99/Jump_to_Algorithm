import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬

# Union-find
parent = [i for i in range(v+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    A = get_parent(a)
    B = get_parent(b)
    if A < B:
        parent[B] = A
        print("union_if", A, B, parent)
    else:
        parent[A] = B
        print("union_else", A, B, parent)

def same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0
for x, y, z in edges:
    if not same_parent(x, y):  # 사이클이 없다면
        print("if not", x, y)
        union_parent(x, y)
        answer += z
print(answer)

import sys
input = sys.stdin.readline

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
    else:
        parent[A] = B


n = int(input())
m = int(input())
parent = [i for i in range(n)]  # Union-find

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            union_parent(i, j)
            # print(f'{parent} i={i} j={j}')

trip = list(map(lambda x: int(x) - 1, input().split()))
root = parent[trip[0]]

for city in trip[1:]:
    if root != parent[city]:
        print("NO")
        exit()

print("YES")



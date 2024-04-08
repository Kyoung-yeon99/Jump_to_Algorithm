# https://headf1rst.github.io/algorithm/kruskal/


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# result: 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순 정렬을 위해 cost를 튜플의 첫번째 원소로 저장
    edges.append((cost, a, b))

# 간선을 오름차순으로 정렬
edges.sort()


# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드 찾을때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클 발생 안하는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

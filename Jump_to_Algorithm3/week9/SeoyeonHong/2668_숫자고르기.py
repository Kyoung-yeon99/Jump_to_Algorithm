# 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램
import sys

input = sys.stdin.readline
answer = []
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)] # 방문 여부

for i in range(1, N+1):
    graph[int(input())].append(i)

def check_cycle(node, route):
    visited[node] = True
    route.append(node)
    for v in graph[node]: # 이어지는 노드에 대해서
        if v not in route: # 사이클을 이루지 않을 경우
            check_cycle(v, route.copy())
        else: # 사이클을 이룰 경우
            answer.extend(route) # 정수 뽑기
            return
            
for i in range(1, N+1):
    if not visited[i]:
        check_cycle(i, [])

answer.sort() # 오름차순 정렬
print(len(answer))
for a in answer:
    print(a)
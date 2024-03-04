# 모든 문제를 먼저 푸는 것이 좋은 문제, 쉬운 문제 먼저 푸는 순서
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split()) # 문제의 수, 정보의 개수
graph = [[] for _ in range(N+1)]
indegree = [0 for i in range(N+1)] # indegree[i]: i번째 문제의 선수 문제 개수
q = []
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1 # A를 먼저 풀고 B를 풀어야 함
    graph[A].append(B)

for i in range(1, N+1):
    if indegree[i] == 0: # 선수 문제가 없는 경우
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q) 
    ans.append(cur)
    for i in graph[cur]: # 현재 문제를 풀고 나서 풀어야 하는 문제들에 대하여
        indegree[i] -= 1 # 선수 문제 개수 감소
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(*ans)
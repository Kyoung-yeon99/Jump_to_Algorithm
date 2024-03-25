# 연결된 노드의 수
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 노드의 수
M = int(input()) # 간선의 개수
al = [[] for _ in range(N+1)] # 인접 노드 리스트

for _ in range(M):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

num = 0
visited = [False for _ in range(N+1)] # 방문 여부
q = deque()
q.append(1)
visited[1] = True

while q: # 연결된 모든 노드 탐색
    next = q.popleft()
    num += 1
    for c in al[next]:
        if not visited[c]:
            visited[c] = True
            q.append(c)

print(num-1) # 연결된 노드의 수 출력(1 제외)


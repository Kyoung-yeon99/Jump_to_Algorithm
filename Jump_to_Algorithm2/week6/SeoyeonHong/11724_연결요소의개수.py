# 무방향 그래프의 연결 요소 개수 구하기
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split()) # 정점의 개수, 간선의 개수
al = {i: [] for i in range(1, N+1)}
count = 0

for _ in range(M):
    u, v = map(int, input().split()) # 간선의 양 끝점
    al[u].append(v)
    al[v].append(u)

q = deque()
left = deque([i for i in range(1, N+1)])

while left: # 모든 요소를 확인할 때 까지
    i = left.popleft()
    q.append(i)
    while q: # i와 이어진 모든 요소 탐색
        n = q.pop()
        for j in al[n]:
            if j in left:
                q.append(j)
                left.remove(j)
    count += 1
    
print(count)
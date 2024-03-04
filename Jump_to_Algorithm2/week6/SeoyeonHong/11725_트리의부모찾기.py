# 각 노드의 부모 구하기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
e = {i: [] for i in range(1, N+1)} # 딕셔너리 구조의 인접 리스트
p = [0 for _ in range(N+1)] # p[i] == i번째 노드의 부모 노드 번호
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    e[v1].append(v2)
    e[v2].append(v1)

visited[1] = True # 1번 노드부터 시작
q = deque([1])

while q:
    parent = q.pop()
    for child in e[parent]: # 현재 노드와 연결된 모든 자식 노드에 대해서
        if not visited[child]: # 아직 확인하지 않은 노드일 경우
            p[child] = parent # 부모 노드 저장
            q.append(child) # 다음으로 탐색할 노드애 자식 노드 추가
    visited[parent] = True # 확인 여부 저장

for n in p[2:]: # 1번부터 시작하므로 0번 제외
    print(n)
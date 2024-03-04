# 루트노드가 없는 트리
# 루트를 1이라고 할 때 각 노드의 부모 구하기.

'''
루트: 1
트리 순회 -> 노드의 개수가 십만이므로 -> bfs이용
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
# 트리 만들기
graph = [[0] for _ in range(n + 1)]  # 노드는 n까지 이므로 n+1
# 방문 체크
visited = [False for _ in range(n + 1)]  # 1차원 리스트
# 정답 리스트
answer = [0 for _ in range(n + 1)]

# 입력
for _ in range(n - 1):  # 1은 제외
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 무방향 == 양방향


def bfs(graph, start, visited):
    que = deque([start])  # start point
    visited[start] = True
    while que:  # 큐가 빌때까지
        v = que.popleft()  # 큐에서 노드(정점)를 꺼낸 다음
        # 해당 원소와 연결된, 아직 방문하지 않은 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                answer[i] = v  # 정답 리스트에 담는다
                visited[i] = True


# 루트 노드는 1
bfs(graph, 1, visited)

for i in range(2, n + 1):  # 2번 노드부터 시행
    print(answer[i])

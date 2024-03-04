# 난이도 순서로 출제된 문제 1~n개
# 선행 문제 존재.
# 3가지 조건
# 1. N개의 문제는 모두 풀어야
# 2. 먼저 푸는 것이 좋은 문제는, 반드시 먼저 풀어야
# 3. 가능하면 쉬운 문제부터 풀어야 함.


# 방향그래프 -> 방향을 거스르지 않고 나열 : 위상정렬(순서가 있는 것들을 순서대로 나열하기)
# 우선순위 큐
# https://toload.tistory.com/entry/JAVA-%EB%B0%B1%EC%A4%80-1766-%EB%AC%B8%EC%A0%9C%EC%A7%91

import heapq

n, m = map(int, input().split())

# 위상정렬 그래프
graph = [[] for _ in range(n + 1)]  # 1-based
# 진입 차수 리스트
indegree = [0 for _ in range(n + 1)]
# 우선순위 큐
que = []

# 선수문제
for _ in range(m):
    first, last = map(int, input().split())
    graph[first].append(last)
    indegree[last] += 1  # 진입차수 + 1 해준다


# 위상정렬
def topology_sort():
    # 정답 담을 리스트
    res = []
    # 1. 진입 차수가 0인 노드부터 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(que, i)
    # 2. 큐가 빌때까지 반복
    while que:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(que)  # 오름차순 정렬 후 추출
        res.append(now)
        # 2-1. 해당 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
        for j in graph[now]:
            indegree[j] -= 1
            # 2-2. 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                heapq.heappush(que, j)
    # 위상정렬 수행한 정답 출력
    for r in res:
        print(r, end=' ')


topology_sort()

# BFS로 풀겠음
# x->y로 변환하는 최소연산횟수를 구해야 하므로, 최단경로에 적합한 BFS 사용
# BFS 특징
# 1. 최단 경로 보장: 너비 우선 탐색으로, 현재 상태에서 가능한 모든 연산 수행 -> 처음으로 y에 도달하는 경로가 최단 경로
# 2. 모든 경우 탐색: BFS는 모든 가능한 상태를 큐에 저장해 탐색 -> 중복 코드는 한번만 방문해 효율적임. x->y로 변환하는 모든 방법 탐색이 중요함

from collections import deque


def solution(x, y, n):
    answer = 0
    # 1. 큐 초기화
    q = deque()
    q.append((x, 0))  # 시작값: x, 연산횟수: 0
    visited = set([x])  # 방문 배열 초기화-> 중복 없으므로 집합 사용

    # 2. 큐 탐색
    while q:
        val, cnt = q.popleft()

        # 1) 목표값에 일치하는 지 확인
        if val == y:
            return cnt
        # 2) 가능한 연산 수행
        for next_val in (val + n, val * 2, val * 3):
            if next_val <= y and next_val not in visited:
                q.append((next_val, cnt + 1))
                visited.add(next_val)

    # 목표값에 도달하지 못한 경우->예외처리
    return -1

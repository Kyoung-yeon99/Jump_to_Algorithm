from collections import deque


def solution(maps):
    answer = []

    # 상하좌우 탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1차원 배열 -> 탐색 위해 2차원 배열로
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    # 순회
    for i in range(n):
        for j in range(m):
            # 바다 or 방문 했을 경우
            if maps[i][j] == 'X' or visited[i][j]:
                continue
            q = deque([(i, j)])  # 튜플을 요소로 갖는 리스트를 사용해야함
            # 현재 노드 방문처리
            visited[i][j] = 1
            # 식량 합 갱신
            sum_food = int(maps[i][j])

            # 큐 순회
            while q:
                # 큐에서 하나씩 원소 추출
                v = q.popleft()
                # 상하좌우로 연결된 땅 확인
                for k in range(4):
                    nx, ny = v[0] + dx[k], v[1] + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = 1  # 방문처리
                        q.append((nx, ny))  # 큐 삽입
                        sum_food += int(maps[nx][ny])  # 식량 합 추가
            answer.append(sum_food)

    if not answer:
        return [-1]
    return sorted(answer)
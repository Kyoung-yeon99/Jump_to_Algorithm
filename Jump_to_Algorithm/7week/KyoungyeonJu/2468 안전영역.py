from collections import deque
n = int(input())
m = []
max_rain = 0
for i in range(n):
    new_l = list(map(int, input().split()))
    m.append(new_l)
    if max_rain < max(new_l):
        max_rain = max(new_l)
"""
max(graph) 는 각 리스트의 첫 번째 원소를 비교해 (list_1[0], list_2[0] ... list[n] 비교) 가장 큰 값을 가진 리스트를 통째로 반환
따라서 max(max(graph))는 "첫 원소가 가장 큰 리스트"에 속한 가장 큰 값을 반환하게 됩니다.
max_rain = max(max(m)) <- 오류!!!!!!
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b, rain, visited):
    qu = deque()
    qu.append((a, b))
    visited[a][b] = 1
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 확인
                if m[nx][ny] > rain and visited[nx][ny] == 0:  # 높이가 강수량 초과인지 확인, 방문 확인
                    visited[nx][ny] = 1
                    qu.append((nx, ny))


result = 0
for x in range(max_rain):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] > x and visited[i][j] == 0:
                bfs(i, j, x, visited)
                cnt += 1

    result = max(result, cnt)

print(result)


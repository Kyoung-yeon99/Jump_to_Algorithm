# https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-3055-%ED%83%88%EC%B6%9C-BFS


from collections import deque

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

for y in range(R):
    for x in range(C):
        if map[y][x] == '*':  # 물 좌표를 앞에 추가
            q.appendleft((y, x))
        elif map[y][x] == 'S':  # 고슴이 좌표 추가
            q.append((y, x))
            visited[y][x] = 0  # 출발점에 시간 0 저장

while q:
    y, x = q.popleft()
    cur = map[y][x]  # 현재 위치
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]  # 다음에 갈 좌표

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 범위 밖이면 무시
            continue
        if visited[ny][nx] != -1:  # 이미 방문한 곳 무시
            continue
        if map[ny][nx] == "*":  # 물 무시
            continue
        if map[ny][nx] == "X":  # 돌 무시
            continue
        if cur == "*" and map[ny][nx] == "D":  # 물이 비버네 가려면 무시
            continue

        if cur == "S":
            if map[ny][nx] == "D":  # 고슴이가 가려는 위치가 비버네면 도착
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1  # 비버네가 아니면 도착 시간 기록

        map[ny][nx] = cur  # 다음 좌표를 고슴이 or 물로 변경
        q.append((ny, nx))  # 다음 탐색 위치 추가
    else:
        continue
    break
else:
    print("KAKTUS")

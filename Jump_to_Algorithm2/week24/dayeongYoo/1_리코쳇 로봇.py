# 한 칸씩 이동하는 것이 아니라 D(장애물) 직전 까지 가거나 맨 끝까지 가는 것이 한 번 움직이는 것
from collections import deque


def solution(board):
    rows, cols = len(board), len(board[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # R의 위치를 찾는다.
    start_row, start_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "R":
                start_row, start_col = i, j
                break

    def bfs():
        dx = [1, -1, 0, 0]  # 상하좌우 방향 이동 배열
        dy = [0, 0, 1, -1]
        queue = deque([(0, start_row, start_col)])  # 이동 횟수와 시작 위치를 큐에 추가
        min_steps = float('inf')  # 최소 이동 횟수를 무한대로 초기화

        while queue:
            steps, cur_row, cur_col = queue.popleft()  # 큐에서 현재 위치와 이동 횟수를 꺼냄
            if visited[cur_row][cur_col]:
                continue  # 이미 방문한 위치는 건너뜀
            visited[cur_row][cur_col] = True  # 현재 위치를 방문 처리

            if board[cur_row][cur_col] == "G":
                min_steps = min(min_steps, steps)  # 목표 지점에 도달하면 최소 이동 횟수를 업데이트
                continue

            for direction in range(4):  # 상하좌우 방향으로 이동
                new_row, new_col = cur_row, cur_col
                while True:
                    new_row += dx[direction]
                    new_col += dy[direction]
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or board[new_row][
                        new_col] == "D":
                        new_row -= dx[direction]
                        new_col -= dy[direction]
                        break  # 보드의 경계나 장애물에 도달하면 이동을 멈춤
                if not visited[new_row][new_col]:
                    queue.append((steps + 1, new_row, new_col))  # 새로운 위치를 큐에 추가

        return min_steps

    answer = bfs()
    return answer if answer != float('inf') else -1  # 최소 이동 횟수를 반환, 불가능하면 -1 반환

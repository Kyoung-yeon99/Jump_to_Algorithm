# 연구소 nxm 직사각형
# 빈 칸, 벽
# 칸에는 바이러스 존재
# 상하좌우 인접한 칸으로 퍼짐
# 3개의 벽을 세워 바이러스 막기 --> 바이러스가 퍼지지 않도록 벽을 어떻게 세울지가 point
# 0: 빈칸, 1: 벽, 2: 바이러스
# 벽 3개 세운 뒤 바이러스가 퍼질 수 없는 곳: 안전 영역
# 안전 영역의 최댓값?

from collections import deque
import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전영역 크기
ans = 0


# 바이러스 퍼뜨리기
def bfs():
    global ans
    q = deque()
    tmp = copy.deepcopy(board)  # 바이러스 퍼뜨리기 전 배열 깊은 복사

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append([i, j])  # 바이러스를 큐에 넣는다(여기서 부터 너비 탐색 시작)
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 0:  # 빈칸이면 바이러스 퍼뜨리기
                    tmp[nx][ny] = 2
                    q.append([nx, ny])  # 큐에 삽입
    # 벽 개수 세기
    cnt = 0
    for t in tmp:
        cnt += t.count(0)  # 안전영역 개수 세기

    ans = max(ans, cnt)


# 벽 세우기(모든 경우의 수 탐색-백트래킹)
def wall(cnt):
    if cnt == 3:  # 벽 3개라면 바이러스 퍼뜨려보기
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:  # 빈칸이라면
                board[i][j] = 1  # 벽 세우기
                wall(cnt + 1)  # 다음 벽 세우러 가기
                board[i][j] = 0  # 벽 허물기(백트래킹)


wall(0)
print(ans)

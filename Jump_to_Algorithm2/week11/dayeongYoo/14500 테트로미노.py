# https://cijbest.tistory.com/m/87
# https://www.acmicpc.net/source/77026865

# 종이 세로, 가로
n, m = map(int, input().split())
# 2차원 배열: 종이 맵
board = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열: visited
visited = [[False] * m for _ in range(n)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최댓값 저장 변수
max_val = 0


# dfs 함수
def sol(x, y, d_sum, cnt):
    global max_val

    # 테트로미노 도형 개수 최대 4개가 완성되면
    if cnt == 4:
        max_val = max(max_val, d_sum)
        return max_val

    # 도형 4개 완성 안 되었다면 dfs 수행
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 체크할때 n, m
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True

            # 보라색 테트로미노(ㅗ)를 만들기 위해 2번째 칸에서 탐색 한번 더 진행
            if cnt == 2:
                sol(x, y, d_sum + board[nx][ny], cnt + 1)
                # 탐색후 방문 취소(원상복귀)
                visited[nx][ny] = False

            sol(nx, ny, d_sum + board[nx][ny], cnt + 1)
            # 세로로 긴 작대기(ㅣ) 모양을 순회 안하는데...?
            print(f"i: {nx}, j: {ny}, board[i][j]: {board[nx][ny]},d_sum: {d_sum + board[nx][ny]} ")
            visited[nx][ny] = False


# 함수 실행
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        sol(i, j, board[i][j], 1)
        visited[i][j] = False
print(max_val)

import sys

sys.setrecursionlimit(10 ** 8)

m, n, k = map(int, input().split())
# 전체 영역을 1로 표시
board = [[True] * n for _ in range(m)]

for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            # 데카르트 좌표계임에 주의(i,j 순서 바뀜)
            board[j][i] = False  # 직사각형 영역은 -1
# print(board)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def dfs(x, y):
    # 직사각형 넓이 저장
    s = 1  # 영역 개수 초기화
    # print(s)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # print(nx, ny)
        if in_range(nx, ny) and board[nx][ny]:  # 직사각형이 아닌 영역이라면
            # 방문체크
            board[nx][ny] = False
            s += dfs(nx, ny)

    return s


# 직사각형 저장
ans = []
for i in range(m):
    for j in range(n):
        # i,j 순서 주의
        # j,i 순으로 찍었을때 올바르게 나오는데, 막상 for문 돌릴 때는 i,j순으로 넣는 이유?
        # print(f'i, j: {j}, {i}')
        if board[i][j]:  # 직사각형이라면 dfs 실행
            # 방문체크
            board[i][j] = False
            ans.append(dfs(i, j))

print(len(ans))
ans.sort()
print(*ans)

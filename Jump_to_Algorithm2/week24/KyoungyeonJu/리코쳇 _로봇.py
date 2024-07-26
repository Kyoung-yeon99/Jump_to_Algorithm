from collections import deque


def solution(board):
    # 격자모양 게임판 위에서 말 움직이기
    # 시작 위치에서 목표 위치까지 최소 몇 번만에 도달하는지
    # 상하좌우 중 하나 선택, 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것이 한 번의 이동
    # 시작 R, 장애물 D, 목표 G, 빈 공간 .
    def bfs(i, j):
        q = deque()
        q.append([i, j, 0])
        visited[i][j] = True

        while q:
            r, c, cnt = q.popleft()

            # 목표 위치인 경우
            if board[r][c] == 'G':
                print("목표 위치", cnt)
                return cnt

            for k in range(4):
                nr, nc = r, c

                while True:
                    nr, nc = nr + dx[k], nc + dy[k]

                    # 범위를 넘어가거나 장애물 위치에 있는 경우
                    if nr < 0 or nr >= h or nc < 0  or nc >= w or board[nr][nc] == 'D':
                        nr, nc = nr - dx[k], nc - dy[k]
                        break

                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append([nr, nc, cnt + 1])

            print()
            print()

        return -1


    h, w = len(board), len(board[0])
    visited = [[False]*w for _ in range(h)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    #obs = set()  # 장애물 위치
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':  # 출발 위치
                start = [i, j]
            elif board[i][j] == 'G':  # 목표 위치
                end = [i, j]
            #elif board[i][j] == 'D':  # 장애물 위치
            #    obs.add((i, j))

    """
    # 답을 찾을 수 없는 경우
    # 목표 위치의 위,아래,좌,우에 장애물이 없는 경우,  끝이 없는 경우
    EXIST_ANSWER = False
   
    # r == 0, c == 3    2, 1
    for a in range(4):
        end_x, end_y = end[0] + dx[a], end[1] + dy[a]
        if 0 <= end_x < h and 0 <= end_y < w:
            if (end_x, end_y) in obs:
                EXIST_ANSWER = True
    if end[0] == 0 or end[0] == (h-1) or end[1] == 0 or end[1] == (w-1):
        EXIST_ANSWER = True

    if not EXIST_ANSWER:
        return -1
    """

    answer = bfs(*start)

    return answer


"""
["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	7
[".D.R", "....", ".G..", "...D"]	-1
".D.R", 
"....", 
".G..", 
"...D"]
"""
#  아래, 왼쪽, 위, 왼쪽, 아래, 오른쪽, 위 순서
tcs = [
    ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."],
    [".D.R", "....", ".G..", "...D"]
]

for tc in tcs:
    print(solution(tc))

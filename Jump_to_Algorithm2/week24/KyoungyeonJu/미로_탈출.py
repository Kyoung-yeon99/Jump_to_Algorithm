from collections import deque

def solution(maps):
    def bfs(s, e, visited):
        x, y = s[0], s[1]
        visited[x][y] = 0
        q = deque()
        q.append([x, y])

        while q:
            r, c = q.popleft()
            #print(r, c, visited[r][c])
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if visited[nr][nc] == -1 and maps[nr][nc] != 'X':
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr, nc])
                    if nr == e[0] and nc == e[1]:
                        return

        return

    h, w = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 시작칸, 레버칸, 탈출칸 구하기
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
            elif maps[i][j] == 'E':
                exit = [i, j]

    # 시작칸에서 레버 칸까지 시간 + 레버 칸에서 탈출칸까지 시간
    visited0 = [[-1] * w for _ in range(h)]
    bfs(start, lever, visited0)
    if visited0[lever[0]][lever[1]] == -1:
        return -1

    visited1 = [[-1] * w for _ in range(h)]
    bfs(lever, exit, visited1)
    if visited1[exit[0]][exit[1]] == -1:
        return -1

    return visited0[lever[0]][lever[1]] + visited1[exit[0]][exit[1]]



"""
def solution(maps):
    def dfs(s, e, cnt, visited):
        #print(f's={s} e={e} cnt={cnt}')
        r, c = s[0], s[1]
        visited[r][c] = cnt

        if s == e:
            return

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == -1 and maps[nr][nc] != 'X':
                    dfs([nr, nc], e, cnt + 1, visited)

        return

    h, w = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 레버 칸까지 시간 + 레버 칸에서 출구까지 시작
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
            elif maps[i][j] == 'E':
                exit = [i, j]

    print(f'start={start} lever={lever} exit={exit}')
    visited0 = [[-1]*w for _ in range(h)]
    dfs(start, lever, 0, visited0)
    if visited0[lever[0]][lever[1]] == -1:
        return -1
    print("first", visited0[lever[0]][lever[1]])
    for i in range(h):
        print(visited0[i])

    visited1 = [[-1] * w for _ in range(h)]
    dfs(lever, exit, 0, visited1)
    if visited1[exit[0]][exit[1]] == -1:
        return -1
    print("second", visited1[exit[0]][exit[1]])
    for i in range(h):
        print(visited1[i])
    return visited0[lever[0]][lever[1]] + visited1[exit[0]][exit[1]]

"""
"""
["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	16
["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	-1
["SOEOL","XXXXO","OOOOO","OXXXX","OOOOO"]   6
["SLEOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"] 2
["SELOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"] 3
["SLXOX", "EXXXO", "OOOOO", "OXXXX", "OOOOO"] 3
["SXXOX", "EXXXL", "OOXOO", "OXXXX", "OOOOO"] -1
["SOOOL", "XXOXX", "XXOOE"] 10
"""


tcs = [
    ["SOEOL", "XXXXO", "OOOOO", "OXXXX", "OOOOO"],
    ["SLEOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"],
    ["SELOX", "XXXXO", "OOOOO", "OXXXX", "OOOOO"],
    ["SLXOX", "EXXXO", "OOOOO", "OXXXX", "OOOOO"],
    ["SXXOX", "EXXXL", "OOXOO", "OXXXX", "OOOOO"],
    ["SOOOL", "XXOXX", "XXOOE"]
]

for tc in tcs:
    print(solution(tc))
    print()
    print()
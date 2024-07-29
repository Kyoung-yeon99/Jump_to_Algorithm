from collections import deque


def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        days = int(maps[x][y])

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        days += int(maps[nr][nc])
                        q.append((nr, nc))

        return days

    answer = []
    h, w = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))

    if not answer:
        answer.append(-1)
    else:
        answer.sort()

    return answer

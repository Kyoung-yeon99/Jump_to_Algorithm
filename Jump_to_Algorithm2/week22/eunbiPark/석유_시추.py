# 0: 빈 땅, 1: 석유
from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    find = [0 for _ in range(m)]
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True

    def bfs(visited):
        cnt = 1
        idxs = set()  # y좌표 저장

        while q:
            x, y = q.popleft()
            idxs.add(y)
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and land[nx][ny] and not visited[nx][ny]:
                    q.append([nx, ny])
                    cnt += 1
                    visited[nx][ny] = 1

        return idxs, cnt

    def calc(idxs, area):
        for id in idxs:
            find[id] += area

    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                q.append([i, j])
                visited[i][j] = 1
                idxs, area = bfs(visited)
                calc(idxs, area)

    return max(find)
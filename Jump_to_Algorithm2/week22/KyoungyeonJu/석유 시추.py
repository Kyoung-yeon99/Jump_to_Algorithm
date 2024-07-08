from collections import deque


def solution(land):
    def bfs(i, j):  # 하나의 석유 덩어리가 차지하는 열과 석유량 return
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        cnt = 0  # 석유량 계산
        visited[i][j] = True
        cols = {j}  # 해당 석유 덩어리가 자치하는 열, 중복 제거를 위해 set 활용
        q = deque()
        q.append([i, j])

        while q:
            r, c = q.popleft()
            cnt += 1
            for a in range(4):
                nr, nc = r + dx[a], c + dy[a]
                if 0 <= nr < n and 0 <= nc < m:
                    if land[nr][nc] == 1 and not visited[nr][nc]:
                        cols.add(nc)  # 석유가 자치하는 column 추가
                        q.append((nr, nc))
                        visited[nr][nc] = True

        return cols, cnt

    n, m = len(land), len(land[0])
    columns = [0] * m  # 각 열에서 시추할 수 있는 석유량
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                cols, cnt = bfs(i, j)
                for c in cols:
                    columns[c] += cnt

    return max(columns)


from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    answer = 0
    campus[x][y] = 'X'
    q = deque()
    q.append((x, y))

    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if campus[nx][ny] != 'X':  # 벽이 아니면
                    if campus[nx][ny] == 'P':  # 친구를 만나면
                        answer += 1
                    campus[nx][ny] = 'X'
                    q.append((nx, ny))

    return answer


n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
Ix, Iy = None, None  # 도연이 위치
campus = []
for i in range(n):
    line = list(input().strip())
    if 'I' in line:
        Ix, Iy = i, line.index('I')
    campus.append(line)

result = bfs(Ix, Iy)
print(result if result != 0 else "TT")


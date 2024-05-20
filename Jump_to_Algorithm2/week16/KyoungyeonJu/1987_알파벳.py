import sys
input = sys.stdin.readline


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:  # 범위 확인
            if maps[nx][ny] not in alphabet:  # 겹치는 알파벳이 없다면
                alphabet.add(maps[nx][ny])  # 알파벳 add
                dfs(nx, ny, cnt+1)
                alphabet.remove(maps[nx][ny])  # 알파벳 remove


r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
answer = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
alphabet = set()
alphabet.add(maps[0][0])
dfs(0, 0, 1)
print(answer)
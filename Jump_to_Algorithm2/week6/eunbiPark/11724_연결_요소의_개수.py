import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [
    []
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

cnt = 0
def dfs(num):
    global cnt
    visited[num] = True
    for b in board[num]:
        if not visited[b]:
            dfs(b)

for i in range(1, n + 1):
    # 방문하지 않은 곳 == 연결되지 않은 곳
    if not visited[i]:
        cnt += 1
        # 연결된 모든 곳 방문하며 방문처리
        dfs(i)

print(cnt)
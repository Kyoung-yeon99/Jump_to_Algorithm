# 0 - 경고 없음, 1 - 경로 있음
# (1, 2) -> 1 : 노드 1 to 노드 2 까지 가는 경로가 있음

n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [0 for _ in range(n)]

'''
# sol_1 - dfs
def dfs(x):
    for i in range(n): # 모든 노드 확인
        # board[x][i]: x (현재 노드)에서 i(확인할 모든 모느)까지 연결 확인
        if board[x][i] == 1 and visited[i] == 0:
            # 이차원 visited가 아닌 이유
            # 시작 노드에 연결된 모든 부분을 판단하기에 (for)
            visited[i] = 1
            dfs(i)

for i in range(n): # 각 노드를 돌며 dfs 돌리기
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end= ' ')
        else:
            print(0, end = ' ')
    print()
    visited = [0 for _ in range(n)]
'''

# sol_2 - 플로이드 와샬
for i in range(n):
    for j in range(n):
        for k in range(n):
            if board[j][i] and board[i][k]:
                board[j][k] = 1

for b in board:
    print(*b)

'''   
# sol_3 - bfs
visited = [[0] * n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and maps[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i) # print 할 때 * 붙이면 [0, 0, 0] -> 0 0 0 으로 출력
'''
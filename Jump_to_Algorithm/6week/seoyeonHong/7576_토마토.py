from collections import deque
import sys
m, n = map(int, input().split()) # 가로칸 m, 세로칸 n
t = []
days = 0
left = 0
for _ in range(n):
    t.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

changed = True
q = deque()
for r in range(n):
    for c in range(m):
        if t[r][c] == 1:
            q.append([r, c])

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4 방향에 대해서
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and t[nr][nc] == 0:
                t[nr][nc] = t[r][c] + 1 # 몇번째 날 익었는지 저장
                q.append([nr, nc])

bfs()
for row in t:
    if 0 in row:
        print(-1)
        exit()
    else:
        days = max(days, max(row))
print(days-1)

    
# 시간 초과
# from collections import deque
# import sys
# m, n = map(int, input().split()) # 가로칸 m, 세로칸 n
# t = []
# days = 0
# left = 0
# for _ in range(n):
#     row = list(map(int, sys.stdin.readline().split()))
#     left += row.count(0)
#     t.append(row)

# visited = [[False for _ in range(m)] for _ in range(n)]
# done = [[False for _ in range(m)] for _ in range(n)]
# changed = True
# q = deque()

# while changed:
#     changed = False
#     for r in range(n):
#         for c in range(m):
#             if t[r][c] == 1 and not visited[r][c]:
#                 visited[r][c] = True
#                 for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4 방향에 대해서
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < n and 0 <= nc < m:
#                         if t[nr][nc] == 0 and not visited[nr][nc]:
#                             q.append([nr, nc])
#                             changed= True

#     while q:
#         pos = q.popleft()
#         r, c= pos[0], pos[1]
#         if not done[r][c]:
#             t[r][c] = 1
#             done[r][c] = True
#             left -= 1

#     if changed:
#         days += 1

# if left == 0:
#     print(days)
# else:
#     print(-1)
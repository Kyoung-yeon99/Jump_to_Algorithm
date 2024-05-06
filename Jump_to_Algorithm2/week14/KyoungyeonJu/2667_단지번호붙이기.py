from collections import deque
import sys
input = sys.stdin.readline


def bfs(r, c, apt_num):
    nums = 1  # 아파트 수
    q = deque()
    q.append([r, c])
    apt[r][c] = apt_num  # 단지 번호
    visited[r][c] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if apt[nx][ny] == 1 and visited[nx][ny] == 0:
                    apt[nx][ny] = apt_num  # 단지 번호
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    nums += 1  # 아파트 수 증가

    return nums


n = int(input())
apt = [list(map(lambda x: int(x), input().rstrip())) for _ in range(n)]
apt_num = 1  # 단지 수
visited = [[0]*n for _ in range(n)]
apt_nums = []  # 단지별 아파트 수
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for r in range(n):
    for c in range(n):
        if apt[r][c] == 1 and visited[r][c] == 0:
            nums = bfs(r, c, apt_num)
            apt_nums.append(nums)
            apt_num += 1

print(apt_num-1)
apt_nums.sort()  # 단지별 아파트 수 오름차순 정렬
for i in range(apt_num-1):
    print(apt_nums[i])

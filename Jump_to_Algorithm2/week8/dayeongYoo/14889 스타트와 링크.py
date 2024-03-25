# 백트래킹을 돌면서 N//2 만큼 팀을 꾸릴 때마다  start, link 변수를 통해 visited 여부를 체크
# 능력치 차이의 최소값을 갱신해
# visited가 1일 경우엔 start 팀으로, 0일 경우엔 link 팀으로 가정하고 구현
# https://yuna0125.tistory.com/211


import sys

input = sys.stdin.readline

n = int(input())
powers = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = 0


def backtracking(cnt, idx):
    global min_diff
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += powers[i][j] + powers[j][i]

                elif not visited[i] and not visited[j]:
                    link += powers[i][j] + powers[j][i]

        min_diff = min(min_diff, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            backtracking(cnt + 1, i + 1)


backtracking(0, 0)
print(min_diff)

# 백트래킹을 돌면서 N//2 만큼 팀을 꾸릴 때마다  start, link 변수를 통해 visited 여부를 체크
# 능력치 차이의 최소값을 갱신해
# visited가 1일 경우엔 start 팀으로, 0일 경우엔 link 팀으로 가정하고 구현
# https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-14889-%ED%95%B4%EC%84%A4-python-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC


import sys

input = sys.stdin.readline

n = int(input())
powers = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = float('inf')


def backtracking(cnt, idx):
    global min_diff
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += powers[i][j]

                elif not visited[i] and not visited[j]:
                    link += powers[i][j]

        min_diff = min(min_diff, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            backtracking(cnt + 1, i + 1)
            visited[i] =0


backtracking(0, 0)
print(min_diff)

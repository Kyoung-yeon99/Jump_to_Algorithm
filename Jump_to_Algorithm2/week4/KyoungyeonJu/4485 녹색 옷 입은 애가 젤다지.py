import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstart(n):
    rupee = [[INF] * n for _ in range(n)]  # 최소 금액 정보
    rupee[0][0] = matrix[0][0]  # 시작값 초기화
    qu = []
    heapq.heappush(qu, (matrix[0][0], 0, 0))  # 최소힙 - 해당 좌표의 값이 작은 게 우선순위, 위치 좌표

    while qu:
        d, x, y = heapq.heappop(qu)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if rupee[nx][ny] > d + matrix[nx][ny]:
                    rupee[nx][ny] = d + matrix[nx][ny]
                    heapq.heappush(qu, (rupee[nx][ny], nx, ny))

    return rupee[n-1][n-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

while True:
    cnt += 1
    n = int(input())
    if n == 0:
        exit(0)

    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(f"Problem {cnt}: {dijkstart(n)}")


# 개인적 질문: 다익스트라는 bfs+dp이다?
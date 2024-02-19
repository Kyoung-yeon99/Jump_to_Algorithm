# 항상 내리막길로 이동하는 경로의 개수

# dfs + dp
# dfs 만으로 푼다면 무수히 많은 경우의 수 등장
# dp 조건: 전체 문제의 최적해가 부분 문제의 최적해로 나누어 지는가
    # 시작점 -> 도착점 문제를 시작점 -> 임의의 (x, y) 문제로 변경하면
    # 해당 경우의 수는 다시 구할 필요가 없다

# 즉, 도착 지점까지 가는 경우의 수 == 도착 지점이 아닌 임의의 점들에서 도착지점까지 가는 경우의 수를 합한 값

# dp 테이블을 만들고
# dp 테이블이 갱신되지 않은 부분을 만나면 해당 지점부터 도착 지점까지 경로의 수 업데이트
# dp 테이블이 갱신되어 있다면 해당 dp 테이블의 값을 바로 반환

# 10억회 -> 한계 걸어야 함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

m, n = map(int, input().split())

maps = []
for _ in range(m):
    maps.append(list(map(int, input().split())))

dp = [[-1] * n for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_range(x, y, now):
    # 위치를 벗어나지 않았는지, 값이 줄어드는 방향으로 이동하는지 판단
    return 0 <= x < m and 0 <= y < n and maps[x][y] < now

def solution(x, y):
    # 도착
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] == -1: # dp 테이블 갱신 전
        dp[x][y] = 0 # 방문처리
        # 상하좌우 방문
        for i in range(4):
            dr_x, dr_y = x + dx[i], y + dy[i]
            if is_range(dr_x, dr_y, maps[x][y]):
                # dp 값 누적 합으로 갱신
                dp[x][y] += solution(dr_x, dr_y)

    # 마지막 위치 반환
    return dp[x][y]

print(solution(0, 0))
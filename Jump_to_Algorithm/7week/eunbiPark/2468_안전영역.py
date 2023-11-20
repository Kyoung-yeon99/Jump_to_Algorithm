# 재귀함수 범위 늘리기
import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

res = []

# 상하좌우돌며 제시된 값보다 큰 연결된 지역 확인
def dfs(x, y, rain, visited):
    # 예외처리
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 상하좌우 돌기
    if graph[x][y] > rain and visited[x][y] == False:
        # 방문처리
        visited[x][y] = True
        dfs(x, y - 1, rain, visited)
        dfs(x, y + 1, rain, visited)
        dfs(x - 1, y, rain, visited)
        dfs(x + 1, y, rain, visited)
        return True
    return False

maximun = max(map(max, graph))
# minimum = min(map(min, graph))

    # minimum 부터 반복하면 minimum 보다 작은 값일 때 판단할 수 없음
# for k in range(minimum, maximun + 1):
for rain in range(maximun + 1):
    visited = [([False] * (n + 1)) for _ in range(n + 1)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain, visited):
                cnt += 1
    res.append(cnt)

print(max(res))
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속
# 1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면, 두 나라가 공유하는 국경선을 하루 동안 연다
# 2. 위의 조건에 의해 열려야 하는 국경선이 모두 열렸다면, 인구 이동 시작
# 3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라는 하루 동안 연합이다
# 4. 연합을 이루고 있는 각 칸의 인구 수는 (연합의 인구수)/(연합을 이루는 칸의 개수). 소수점 버리기
# 5. 연합 해체하고 국경선 닫기
from collections import deque

def movement(x, y):
    visited_territory = [(x, y)]
    sum_population = matrix[x][y]
    qu = deque()
    qu.append((x, y))
    visited[x][y] = True

    while qu:
        r, c = qu.popleft()

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(matrix[r][c] - matrix[nr][nc]) <= R:
                    qu.append((nr, nc))
                    visited_territory.append((nr, nc))
                    visited[nr][nc] = True
                    sum_population += matrix[nr][nc]

    return sum_population, visited_territory


N, L, R = map(int, input().split())  # 1 <= N <= 50, 1 <= L <= R <= 100
matrix = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

while True:
    visited = [[False]*N for _ in range(N)]
    is_union_formed = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                sum_population, visited_territory = movement(i, j)
                if len(visited_territory) > 1:
                    is_union_formed = True
                    avg_population = sum_population // len(visited_territory)
                    for x, y in visited_territory:
                        matrix[x][y] = avg_population

    if not is_union_formed:
        break

    answer += 1

print(answer)
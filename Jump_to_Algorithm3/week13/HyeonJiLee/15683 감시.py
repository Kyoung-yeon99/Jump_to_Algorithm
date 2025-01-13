import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# CCTV 위치 찾기
cctv = [(i, j, arr[i][j]) for i in range(N) for j in range(M)\
        if 1 <= arr[i][j] <= 5]

# CCTV 방향 정의
cctv_direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]], #상하 좌우
    3: [[0, 2], [0, 3], [1, 2], [1, 3]], #좌상 좌하 우상 우하
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(arr, cctv, id):
    if id == len(cctv):
        #모든 cctv 확인했으면 사각지대 개수 세서 반환
        return sum(row.count(0) for row in arr)

    x, y, cctv_num = cctv[id]
    min_count = 65 # 8*8 크기 + 1

    for direction in cctv_direction[cctv_num]:
        tmp = copy.deepcopy(arr)
        #각 방향마다 탐색
        for d in direction:
            next_x, next_y = x, y
            while True:
                next_x += dx[d]
                next_y += dy[d]
                if (next_x < 0 or next_x >= len(arr) or next_y < 0 or next_y >= len(arr[0]))\
                        or tmp[next_x][next_y] == 6:
                    # 좌표가 범위 안에 있지 않거나 벽만나면 더이상 해당 방향으로 이동 X
                    break
                if tmp[next_x][next_y] == 0:  # tmp에 마킹
                    tmp[next_x][next_y] = '#'
        #재귀 호출
        blind_spots = dfs(tmp, cctv, id + 1)
        min_count = min(min_count, blind_spots)

    return min_count

result = dfs(arr, cctv, 0)
print(result)

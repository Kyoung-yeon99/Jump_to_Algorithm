# 삼성 기출

# 청소하는 영역의 개수 구하기
# 청소되지 않은 경우 청소
# 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    # 후진 가능 - 후진 후 청소
    # 후진 불가 - 종료
# 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    # 반시계 방향으로 90도 회전
    # 앞쪽 칸이 청소되지 않은 경우 한 칸 전진
    # 청소

n, m = map(int, input().split())
# (r, c) : 현재 청소기 좌표, d : 방향 (0: 북, 동, 남, 서)
r, c, d = map(int, input().split())
maps = [] # 0: 청소되지 않은 곳
for _ in range(n):
    maps.append(list(map(int, input().split())))

count = 0
# step1. 0인 부분 세는 dfs 코드 작성
# step2. 1일 때 후진하는 코드 작성
# step3. 1일 때 회전하는 코드 작성

def dfs(x, y, v):
    global count # 청소한 영역의 개수
    # 북, 동, 남, 서
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    # 청소되지 않은 경우, 청소
    if maps[x][y] == 0:
        maps[x][y] = 2 # 방문 처리
        count += 1

    # 주변 청소 여부 확인
    for _ in range(4):
        # 바라보는 방향 변경
        # d = (d - 1) % 4
        nv = (v + 3) % 4
        # 회전
        dx = x + dxs[nv]
        dy = y + dys[nv]

        # 전진 전 청소 여부 확인
        if maps[dx][dy] == 0:
            # 전진
            # 1번으로 돌아가기
            dfs(dx, dy, nv)
            return
        v = nv
    # 후진
    nv = (v + 2) % 4
    dx = x + dxs[nv]
    dy = y + dys[nv]

    # 벽이면 리턴
    if maps[dx][dy] == 1:
        return
    # 벽 아니면 1번으로
    dfs(dx, dy, v)

dfs(r, c, d)
print(count)
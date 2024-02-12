dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]  # 북 동 남 서

n, m = map(int, input().split())  # 방 크기
r, c, d = map(int, input().split())  # 처음 위치, 바라보는 방향
room = [list(map(int, input().split())) for _ in range(n)]

room[r][c] = -1  # -1 청소 끝난 상태
cnt = 1
while room[r][c] != 1:  # 벽이 아니라면
    flag = False
    for _ in range(4):  # 현재 칸의 주변 4칸 확인
        d -= 1  # 반시계 방향 90도 회전이므로 -1
        if d == -1:  # d: 0은 북쪽, 1은 동쪽, 2은 남쪽, 3은 서쪽
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]
        if room[nr][nc] == 0:  # 청소가 되지 않은 빈 칸이 있다면
            r, c = nr, nc
            room[r][c] = -1  # 청소 완료
            cnt += 1  # 청소한 칸 개수 증가
            flag = True
            break
    if not flag:  # 청소가 되지 않은 빈 칸이 없다면
        r += dr[d-2]  # 후진 방향(정반대) -2
        c += dc[d-2]  # 후진 방향(정반대) -2

print(cnt)

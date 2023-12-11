n = int(input())

# 지뢰
bomb = []
for _ in range(n):
    lines = input().split('\n')  # 개행문자를 기준으로 문자열 분리해 리스트화
    for line in lines:
        bomb.append(list(line))

# 게임판
play = []
for _ in range(n):
    lines = input().split('\n')  # 개행문자를 기준으로 문자열 분리해 리스트화
    for line in lines:
        play.append(list(line))

# 상하좌우, 대각선 탐색
dxs = (1, -1, 0, 0, 1, -1, -1, 1)
dys = (0, 0, 1, -1, 1, 1, -1, -1)
# 지뢰 방문 체크
visited = False

for i in range(n):
    for j in range(n):
        if play[i][j] == 'x':  # x: 열린 칸
            if bomb[i][j] == '*':
                # 지뢰 밟으면 별표로 표시
                visited = True
            cnt = 0  # 지뢰 카운트
            for l in range(8):  # 8방 탐색
                nx, ny = i + dxs[l], j + dys[l]
                # print(nx, ny)
                if 0 <= nx < n and 0 <= ny < n and bomb[nx][ny] == '*':
                    cnt += 1
                play[i][j] = str(cnt)  # 문자열 join을 위해
# 지뢰 체크
if visited:  # 지뢰 있는 칸이 열렸으면 지뢰가 있는 모든 칸 '*' 표시
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                play[i][j] = '*'

# 정답
ans = 0
for p in play:
    ans = "".join(p)
    print(ans)

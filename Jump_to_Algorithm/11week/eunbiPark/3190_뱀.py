# https://www.acmicpc.net/problem/3190
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apple = [] # 사과 위치
for _ in range(k):
    apple.append(list(map(int, input().split())))
l = int(input())
move = [] # 이동 시간, 방향
for i in range(l):
    x, c = input().split()
    move.append((int(x), c))

# 방향 설정
# 우 하 좌 상
# L: 인덱스 감소, D: 인덱스 증가
# 처음 위치 동쪽, 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# board 설정
board = [[0] * (n + 1) for _ in range(n+1)]
# 사과 위치 설정 (1: 사과 있음)
for i, j in apple:
    board[i][j] = 1

def turn(direction, c): # 현재 방향, 전환 방향
    if c == 'L':
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4
    return direction


def simulate():
    # 시작 위치 설정
    x, y = 1, 1
    # 뱀위 위치 : 2
    board[x][y] = 2
    direction = 0
    time = 0
    idx = 0 # 다음 회전 정보
    q = [(x, y)] # 뱀, 뱀이 지나가면 map 을 0으로 변경

    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있고, 몸에 부딪히지 않는다면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과나 뱀의 몸이 없다면
            if board[nx][ny] == 0:
                # 몸이 있다고 표시
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0) # 꼬리 떼어내기
                board[px][py] = 0 # 꼬리를 맵에서 지운다

            # 사과가 있다면
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        # 충돌
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1

        # 회전할 타이밍 확인
        if idx < l and move[idx][0] == time:
            direction = turn(direction, move[idx][1])
            idx += 1
    return time





# 1. 머리를 다음 칸으로
# 2. 부딪히면 end (벽, 몸)
# 3. if(사과):
    # 사과 없애고, 꼬리 이동 (x)
# 4. else:
    # 몸길이 줄여 꼬리가 위치한 칸 비우기 (길이 변화 x)

print(simulate())
# 1. 그래프(맵)을 모두 0으로 채움
# 2. 사과 위치는 모두 2로 채움
# 3. 앞으로 뱀이 차지하고 있는 부분은 1로 채움
# 4. 뱀이 이동할 때 마다 머리와 꼬리는 한 칸 씩 전진(몸의 길이는 그대로)
# 5. 이동했을 때 사과를 먹으면 머리는 전진, but 꼬리는 그대로(몸의 길이가 한 칸씩 증가)
# 6. 방향전환을 해야 하는 타이밍에 맞춰 L->왼쪽, D->오른쪽 방향전환

# 4번: 처음 시작할 때 [0,0]을 큐에 넣어 몸길이 1 뱀의 초기 위치 상태 저장
# 오른쪽으로 한칸 이동 -> [0,0]을 큐 pop -> [0,1]을 큐 push-> 뱀의 위치 상태 변경
# 이런식으로 뱀 전진 -> 큐를 뱀의 몸을 나타낸다고 생각하자

# 5번: graph[x][y] = 2일때 -> 머리만 전진하면 되므로 큐에서 pop x
# 큐의 현재 머리 위치만 push -> 뱀의 몸길이 늘려줌

# 6번: 방향전환을 해야 한다면 입력한 방향에 맞게 전환을 해주면 됨
# 딕셔너리 키: 시간, 값: 방향

from collections import deque

# 보드 크기
n = int(input())
# 뱀이 이동할 보드 만들기
board = [([0] * n) for _ in range(n)]
# 사과의 위치 입력받기
apple = []
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    # 문제의 맨위 좌측 (1,1) -> 보드에서는 (0,0)으로 위치 변환
    a_row, a_col = row - 1, col - 1
    # 사과 위치를 나타내는 1을 보드에 표시
    board[a_row][a_col] = 1
    # 사과 리스트에 사과의 위치 좌표 추가
    apple.append((a_row, a_col))

# 뱀의 방향회전
L = int(input())
change_snake = []
for _ in range(L):
    # 뱀의 방향 회전 정보를 리스트에추가
    dis, direct = input().split()
    dis = int(dis)
    change_snake.append((dis, direct))
# 문제에서 주어진 시간은 10000초 이하로 해결
change_snake.append((10001, ''))
# 북, 동, 남, 서 방향 이동
change = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 뱀 방향 전환
def turn_snake(direction):
    global turn_index
    # 왼쪽으로 회전
    if direction == 'L':
        if turn_index != 0:
            turn_index -= 1
        else:
            turn_index = 3
    # 오른쪽으로 회전
    else:
        if turn_index != 3:
            turn_index += 1
        else:
            turn_index = 0
    return


# 게임 전 뱀이 있는 위치
snake = deque()
snake.append((0, 0))
# 게임 시작 시 뱀의 시작방향 : 동쪽
turn_index = 1
# 뱀의 머리 위치
x, y = 0, 0
# 게임 진행시간
cnt = 0
# 방향을 바꿀 때 출발 시간
start = 1
# 반복문 탈출 명령
breaker = False
# 뱀의 방향 정보 입력
for i in range(len(change_snake)):
    # 게임 시작
    start = cnt + 1
    for _ in range(start, change_snake[i][0] + 1):
        # 이동할 좌표 설정
        nx = x + change[turn_index][0]
        ny = y + change[turn_index][1]
        # 이동할 좌표가 벽 또는 자기자신의 몸과 부딪힌다면 반복문 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            cnt += 1
            breaker = True
            break
        # 뱀이 이동할 다음 위치에 사과가 있을 경우
        if board[nx][ny] == 1:
            # 사과먹기
            board[nx][ny] = 0
            x, y = nx, ny
            # 뱀의 위치 표시
            snake.append((x, y))
        # 다음 위치에 사과 x
        else:
            x, y = nx, ny
            # 뱀 위치 표시
            snake.popleft()
            snake.append((x, y))
        # 게임 1초씩 증가
        cnt += 1
    if breaker == True:
        break
    # 뱀 이동후 방향 전환
    turn_snake(change_snake[i][1])
# 정답 출력
print(cnt)

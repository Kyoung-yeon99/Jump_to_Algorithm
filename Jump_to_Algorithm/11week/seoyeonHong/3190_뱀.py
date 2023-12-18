from collections import deque

count, head, body = 0, [1, 1], deque() # 게임 플레이 시간, 뱀의 위치
over = False # 게임 종료 플래그
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
apple = [] # 사과의 위치
for _ in range(k):
    apple.append(list(map(int, input().split())))
l = int(input()) # 뱀의 방향 변환 횟수
move = deque() # 뱀의 방향 전환 정보
direction = deque([(0, 1), (1, 0), (0, -1), (-1, 0)]) # 진행 방향
for _ in range(l):
    t, d = input().split()
    move.append([int(t), d])

def go():
    global count, head, body, direction

    if move and move[0][0] == count: # 방향 전환 필요 시
        if move[0][1] == 'L':
            direction.rotate(1) # 리스트 오른쪽으로 회전
            print("turn left")
        else:
            direction.rotate(-1) # 리스트 왼쪽으로 회전
            print("turn right")
        move.popleft()
    
    count += 1 # 플레이 시간 +1
    head = [head[0] + direction[0][0], head[1] + direction[0][1]] # 진행방향으로 1만큼 이동
    print(f'move to {head}')
    body.append([head[0] - direction[0][0], head[1] - direction[0][1]]) # 뱀 몸 길이 + 1
    
    if head in body or head[0] > n or head[0] < 1 or head[1] > n or head[1] < 1: # 벽이나 자기자신의 몸과 부딪힐 경우
        return False
    
    if head not in apple: # 사과를 먹지 않은 경우
        body.popleft() # 몸길이를 줄여서 꼬리가 위치한 칸 비우기
    else:
        apple.remove(head) # 사과 없애기
    
    return True

while not over: # 게임이 끝날 때 까지
    if not go(): # 한 칸씩 이동
        over = True # 게임이 끝났을 경우 플래그 변경

print(count) # 게임이 몇 초에 끝나는지 출력
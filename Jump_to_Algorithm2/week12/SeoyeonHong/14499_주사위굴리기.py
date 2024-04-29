# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하기
import sys

input = sys.stdin.readline
N, M, x, y, K = map(int, input().split()) # 지도의 가로 세로 크기, 주사위 좌표, 명령 개수
m = [] # 지도
cmd = [] # 명령어
# 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0

for _ in range(N):
    m.append(list(map(int, input().split())))
cmd = list(map(int, input().split()))

for c in cmd:
    nx, ny = x + dx[c], y + dy[c] # 이동할 좌표
    if 0 <= nx < N and 0 <= ny < M: # 지도 안으로 움직일 경우
        if c == 1: # 동쪽으로 이동
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif c == 2: # 서쪽으로 이동
            n1, n3, n4, n6 = n3, n6, n1, n4
        elif c == 3: # 북쪽으로 이동
            n1, n2, n5, n6 = n5, n1, n6, n2
        elif c == 4: # 남쪽으로 이동
            n1, n2, n5, n6 = n2, n6, n1, n5

        # 바닥에 0이 쓰여 있을 경우
        if m[nx][ny] == 0:
            # 주사위 바닥면에 쓰여 있는 수가 칸에 복사
            m[nx][ny] = n6
        # 바닥에 0이 아닌 숫자가 쓰여 있을 경우
        else:
            # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
            n6 = m[nx][ny]
            m[nx][ny] = 0
        
        x, y = nx, ny
        print(n1)

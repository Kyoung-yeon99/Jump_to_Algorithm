import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 방의 크기
r, c, d = map(int, input().split()) # 로봇 청소기 좌표, 방향
state = [] # 방의 상태 - 0: 청소 전, 1: 벽, -1: 청소 후
dx = [-1, 0, 1, 0] # 북, 동, 남, 서 x좌표 차이
dy = [0, 1, 0, -1] # 북, 동, 남, 서 y좌표 차이
left = 0 # 청소되지 않은 칸의 개수
for _ in range(N):
    row = list(map(int, input().split()))
    left += row.count(0)
    state.append(row)
count = 0 # 청소한 칸의 개수

def clear(): # 주변 4칸 중 청소되지 않은 칸이 있는지 확인
    if r > 0 and state[r-1][c] == 0:
        return False
    if c < M - 1 and state[r][c+1] == 0:
        return False
    if r < N - 1 and state[r+1][c] == 0:
        return False
    if c > 0 and state[r][c-1] == 0:
        return False
    return True # 모두 청소되었을 경우

    
while left != 0: # 청소가 다 될 때 까지 작동
    if state[r][c] == 0: # 청소 전일 경우
        state[r][c] = -1 # 현재 칸을 청소
        count += 1 # 청소한 칸 증가
        left -= 1 # 남은 칸 감소
        print("clean", r, c)
    
    # 주변 4칸 확인 및 이동
    if clear(): # 주변이 모두 청소된 칸일 경우
        br = r + dx[(d + 2) % 4]
        bc = c + dy[(d + 2) % 4]
        if (0 <= br < N-1) and (0 <= bc < M-1) and state[br][bc] != 1: # 후진이 가능한 경우
            r, c = br, bc # 후진
            print("go back to", r, c)
        else: # 후진이 불가능할 경우
            print("stop working")
            break # 작동 중지
    else: # 주변에 청소되지 않은 칸이 있는 경우
        for _ in range(4): # 최대 4칸 확인
            d = (d - 1) % 4 # 반시계 방향으로 90도 회전
            fr = r + dx[d]
            fc = c + dy[d]
            if (0 <= fr < N-1) and (0<= fc < M-1) and state[fr][fc] == 0: # 앞쪽 칸이 청소되지 않은 경우
                r, c = fr, fc # 앞으로 이동
                print("rotate and go to", r, c)
                break

print(count) # 청소한 칸의 개수 출력
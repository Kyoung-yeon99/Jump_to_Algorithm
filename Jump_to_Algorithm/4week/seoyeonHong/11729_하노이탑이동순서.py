n = int(input()) # 원판의 개수
global k # 원판을 옮긴 횟수
moves = []

def hanoi(n, start, temp, goal):
    global k
    if n == 1: # 1개 남았을 경우
        moves.append([start, goal]) # 현재 위치에서 목표 위치로 이동
        k += 1 # 이동 횟수 증가
    else:
        hanoi(n - 1, start, goal, temp) # n-1개를 임시 위치로 이동
        hanoi(1, start, temp, goal) # n번째 원반을 목표 위치로 이동
        hanoi(n - 1, temp, start, goal) # n-1개를 목표 위치로 이동

k = 0
hanoi(n, 1, 2, 3)
print(k)
for move in moves:
    print(move[0], move[1])

# 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
step = 0 # 진행 중인 단계
destroyed = 0 # 내구도가 0인 칸의 개수
c = deque([[A[i], False] for i in range(2*N)]) # 컨베이어 벨트

while destroyed < K:
    c.rotate(1) # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    c[N-1][1] = False # 내리는 위치에 있는 로봇은 내리기
    for i in range(N-2, -1, -1):
        if c[i][1] and c[i+1][0] > 0 and not c[i+1][1]: # i번째 칸에 로봇이 있고 다음 칸의 내구도가 1 이상고 비어있을 경우
            c[i][1] = False # i+1로 이동
            c[i+1][1] = True
            c[i+1][0] -= 1 # 내구도 감소
            if c[i+1][0] == 0:
                destroyed += 1

    c[N-1][1] = False # 내리는 위치에 있는 로봇은 내리기

    if c[0][0] > 0: # 올리는 위치에 로봇을 올릴 수 있으면
        c[0][1] = True # 새로운 로봇 올리기
        c[0][0] -= 1
        if c[0][0] == 0:
            destroyed += 1

    step += 1

print(step)


# 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
# 만약 이동할 수 없다면 가만히 있는다.
# 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.

# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.

# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

from collections import deque


n, k = map(int, input().split())
a = list(map(int, input().split()))
belt = deque(a)
robot = deque([False]*n)

cnt = 0
while belt.count(0) < k:
    cnt += 1

    # 회전하기
    belt.rotate(1)
    robot.rotate(1)

    if robot[n-1]:  # 내리기
        robot[n-1] = False

    # 가장 idx가 큰 로봇부터 한 칸 이동
    for i in range(n-2, -1, -1):
        if robot[i]:
            if not robot[i+1] and belt[i+1] >= 1:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1

    if belt[0] != 0:  # 올리기
        robot[0] = True
        belt[0] -= 1

    if robot[n-1]:  # 내리기
        robot[n-1] = False

print(cnt)

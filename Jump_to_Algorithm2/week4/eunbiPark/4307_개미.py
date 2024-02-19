import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stick_len, ant_count = map(int, sys.stdin.readline().split())
    min_time = []
    max_time = []

    for _ in range(ant_count):

        # 현재 개미의 위치
        loc = int(sys.stdin.readline())

        # 현재 개미가 땅으로 떨어지는 최소 시간 저장
        min_time.append(min(loc, stick_len - loc))

        # 현재 개미가 땅으로 떨어지는 최대 시간 저장
        max_time.append(max(loc, stick_len - loc))

    print(max(min_time), max(max_time))
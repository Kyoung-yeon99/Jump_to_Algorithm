'''

1. 이동 허용한 채널의 범위는 0 ~ 500,000
2. 현재 접속 중인 채널 번호 = 100

시작 cnt 는 현재 채널인 100 부터 목표 채널 까지 그냥 +/- 하는 경우.

0 부터 1000000 까지 가능한 번호 숫자 중, 해당 번호에서 +/- 하는 경우.

2가지 경우로 나눠서 풀이
'''


def solution(N, M, broken):
    cnt = abs(N - 100)
    buttons = []

    for i in range(10):
        if i not in broken:
            buttons.append(i)

    if N == 100:
        return 0

    if not buttons:
        return abs(100 - N)

    for i in range(1000001):
        num_list = list(map(int, str(i)))
        valid = True
        for n in num_list:
            if n in broken:
                valid = False
                break

        if valid:
            cnt = min(cnt, len(num_list) + abs(N - i))

    return cnt


# 채널 N
N = int(input())
# 고장난 버튼 개수 M
M = int(input())
# 고장난 버튼이 있는 경우 고장난 버튼, 같은 버튼 x
broken = list(map(int, input().split()))

print(solution(N, M, broken))

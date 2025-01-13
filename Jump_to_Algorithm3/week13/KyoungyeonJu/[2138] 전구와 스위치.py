# N개의 전구들의 현재 상태와 만들고자 하는 상태가 주어졌을 때, 최소 스위치 누르는 횟수

def check(copy):
    cnt = 0
    for i in range(1, n):
        if copy[i-1] == end[i-1]:
            continue

        cnt += 1
        for j in range(i-1, i+2):
            if j < n:
                copy[j] = 1 - copy[j]

    if copy == end:
        return cnt
    else:
        return 1e5


n = int(input())  # 2 ≤ N ≤ 100,000
start = list(map(int, input()))
end = list(map(int, input()))
answer = 1e5
# 스위치를 누르는 순서는 상관 없다 -> 1번 스위치 지정하고 순차적으로 탐색
# i번째 스위치가 i-1번째 전구의 상태를 결정할 마지막 스위치이다
if start == end:
    print(0)
else:
    # 첫 번째 스위치 누르는 경우
    first_on = start[:]
    first_on[0] = 1-start[0]
    first_on[1] = 1-start[1]
    answer = min(answer, check(first_on)+1)

    # 첫 번째 스위치 누르지 않는 경우
    answer = min(answer, check(start))

    if answer == 1e5:
        print(-1)
    else:
        print(answer)
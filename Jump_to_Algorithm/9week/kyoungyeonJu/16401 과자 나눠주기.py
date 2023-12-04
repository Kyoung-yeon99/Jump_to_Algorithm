import sys
input = sys.stdin.readline

m, n = map(int, input().split())  # 조카 수, 과자 수
snack = list(map(int, input().split()))  # 과자 길이
# 조카 수에 맞추어 가장 긴 과자 길이 구하기, 불가능하면 0 출력
# 조카가 과자보다 적으면 상관x
# 조카가 과자보다 많으면 하나를 여러 개로 쪼개야 함
start, end = 1, max(snack)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    #print("mid=", mid)
    for i in snack:
        if i >= mid:
            cnt += (i//mid)
            # print("cnt=", cnt)
    if cnt >= m:  # 과자 개수와 같거나 크면, 길이 늘리기
        start = mid + 1
        # print("max_length=", max_length, "start", start)
    else:  # 작으면, 길이 줄이기
        end = mid - 1
        # print("mid=", mid, "end=", end)

print(end)


""" 둘 다 맞음!
start, end = 1, max(snack)
max_length = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in snack:
        if i >= mid:
            cnt += (i//mid)
    if cnt >= m:  # 과자 개수와 같거나 크면, 길이 늘리기
        max_length = mid
        start = mid + 1
    else:  # 작으면, 길이 줄이기
        end = mid - 1

print(max_length)
"""
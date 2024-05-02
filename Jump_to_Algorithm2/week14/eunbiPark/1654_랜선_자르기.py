k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

lan.sort()

# mid 로 나누었을 때 n개의 랜선을 만들 수 있는지 확인
def calc(mid):
    cnt = 0
    for l in lan:
        cnt += (l//mid)

    if cnt >= n:
        return True
    return False

left = 1
right = lan[-1]

# 가장 짧은 랜선 기준으로 이분 탐색
while left <= right:
    mid = (left + right)//2
    ret = calc(mid)

    if ret: # 가능
        left = mid + 1

    else: # 불가능
        right = mid - 1

print(right)
# m: 조카의 수, n: 과자의 수
m, n = map(int, input().split())
# 과지 길이
snack = list(map(int, input().split()))
# 이분탐색 위해 정렬
snack.sort()

left = 1  # 시작점
right = snack[-1]  # 끝점
ans = 0  # 정답

while left <= right:
    total = 0  # 총 과자의 수
    mid = (left + right) // 2  # 중간점

    for s in snack:
        total += (s // mid)  # 과자//중간값: 최대 과자 길이 구함
    if total >= m:  # 조카 수보다 더 크다면
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)

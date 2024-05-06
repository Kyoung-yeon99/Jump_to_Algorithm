k, n = map(int, input().split())
ropes = [int(input()) for _ in range(k)]
left, right = 1, max(ropes)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in range(k):
        cnt += ropes[i]//mid

    if cnt < n:  # 랜선 길이가 큰 경우 -> 랜선 개수 적음
        right = mid-1
    else:  # 랜선 길이가 작은 경우 -> 랜선 개수 큼
        left = mid + 1

print(right)
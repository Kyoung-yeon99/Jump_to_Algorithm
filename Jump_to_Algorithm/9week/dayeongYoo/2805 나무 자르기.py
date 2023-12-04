n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)  # 높이 0 가능

while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree >= mid:  # 중간값 보다 나무 길이가 더 길다면
            total += tree - mid
    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)

n, m = map(int, input().split()) # 나무 수, 가져가려는 길이
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    temp_sum = 0
    for i in trees:
        if i >= mid:
            temp_sum += i - mid

    if temp_sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
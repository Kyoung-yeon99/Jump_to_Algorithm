N, K = map(int,input().split())
arr = list(map(int, input().split()))
count = dict((i, 0) for i in set(arr))

start, end = 0,0
max_len = 0
while end < N:
    cur = arr[end]
    first = arr[start]

    if count[cur]<K:
        count[cur] += 1
        end += 1
    else:
        count[first] -= 1
        start += 1
    max_len = max(max_len, end-start)
print(max_len)

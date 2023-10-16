from collections import deque

n, m = map(int, input().split())

data = deque([i for i in range(1, n + 1)])
idx = list(map(int, input().split()))

cnt = 0
for num in idx:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data)//2:
                data.rotate(-1)
                cnt += 1
            else:
                data.rotate(1)
                cnt += 1

print(cnt)
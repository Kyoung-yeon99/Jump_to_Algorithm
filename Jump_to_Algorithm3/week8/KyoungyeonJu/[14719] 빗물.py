h, w = map(int, input().split())
answer = 0
block = list(map(int, input().split()))
for i in range(1, w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    m = min(left, right)
    if block[i] < m:
        answer += (m - block[i])

print(answer)

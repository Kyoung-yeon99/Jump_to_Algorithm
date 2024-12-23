N = int(input())
arr = [0 for _ in range(1001)]
max_id = 0
for _ in range(N):
    L, H = map(int, input().split())
    max_id = max(max_id, L)
    arr[L] = H
arr = arr[:max_id+1]
left_max = [0] * len(arr)
right_max = [0] * len(arr)
answer = [0] * len(arr)

left_max[0] = arr[0]
for i in range(1, len(arr)):
    left_max[i] = max(left_max[i-1], arr[i])

right_max[len(arr)-1] = arr[len(arr)-1]
for i in range(len(arr) - 2 , -1, -1):
    right_max[i] = max(right_max[i+1], arr[i])

for i in range(len(arr)):
    answer[i] = min(left_max[i], right_max[i])
print(sum(answer))
N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
min_length = float('inf')

for right in range(N):
    current_sum += arr[right]
    
    while current_sum >= S:  # 부분합이 S 이상이면
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]  # 왼쪽 포인터를 이동
        left += 1

# 결과 출력
print(min_length if min_length != float('inf') else 0)

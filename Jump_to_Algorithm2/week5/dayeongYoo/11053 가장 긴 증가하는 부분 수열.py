n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for cur in range(1, n):
    for front in range(0, cur):  # 범위 주의
        if arr[front] < arr[cur]:  # 앞에 있는게 더 작다면 부분 수열 불가.
            dp[cur] = max(dp[cur], dp[front] + 1)  # 이전 숫자+1
print(max(dp))

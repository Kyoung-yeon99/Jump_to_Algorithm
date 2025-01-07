N = int(input())
arr = [int(input()) for _ in range(N)]

# 연속 증가 부분 수열 길이 계산
dp = [1] * N  # 각 위치에서 끝나는 가장 긴 증가 부분 수열의 길이를 저장

# 동적 계획법으로 증가 부분 수열 길이 계산
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)

# 최소 이동 횟수 = N - 가장 긴 증가 부분 수열 길이
print(N - max_length)

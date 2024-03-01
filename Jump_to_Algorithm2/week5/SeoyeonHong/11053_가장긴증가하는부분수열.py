# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열 구하기
N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] : # A[i]가 가장 큰 부분 수열의 길이 갱신
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 이전 풀이
n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n): 
    for j in range(i-1, -1, -1):
        if seq[i] > seq[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
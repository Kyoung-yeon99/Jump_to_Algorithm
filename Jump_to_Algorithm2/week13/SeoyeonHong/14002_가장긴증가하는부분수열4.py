N = int(input()) # 수열의 크기
A = list(map(int, input().split())) # 수열
asc_seq = [] # 증가하는 수열
dp = [1 for i in range(N)] # dp[i]는 증가하는 수열 [..., i]의 길이

for i in range(1, N):
    num = A[i]
    for j in range(i):
        if num > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
pos = max(dp) # 가장 긴 증가하는 부분 수열의 길이
print(pos)

for i in range(N-1, -1, -1):
    if dp[i] == pos:
        asc_seq.append(A[i])
        pos -= 1

asc_seq.reverse()
print(*asc_seq)

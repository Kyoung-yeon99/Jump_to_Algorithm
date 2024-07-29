# https://school.programmers.co.kr/learn/courses/30/lessons/154538

# x를 y로 변환하기 위해 필요한 최소 연산 횟수
def solution(x, y, n):
    INF = int(1e9) # 최댓값
    dp = {i: INF for i in range(x, y*3+1)} # i: {i로 변환하기 위해 필요한 최소 연산 횟수}
    dp[x] = 0
    for i in range(x, y+1):
        if dp[i] != INF: # 변환 가능하다면 최소 연산 횟수 갱신
            dp[i+n] = min(dp[i]+1, dp[i+n])
            dp[i*2] = min(dp[i]+1, dp[i*2])
            dp[i*3] = min(dp[i]+1, dp[i*3])

    return dp[y] if dp[y] != INF else -1 # 최소 연산 횟수 또는 -1 반환
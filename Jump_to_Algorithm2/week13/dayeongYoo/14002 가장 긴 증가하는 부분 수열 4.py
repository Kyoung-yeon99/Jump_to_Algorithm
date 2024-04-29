# 수열 a의 가장 긴 증가하는 부분 수열
# https://velog.io/@kimdukbae/BOJ-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-Python

# 수열 크기
n = int(input())
# 수열 a
a = list(map(int, input().split()))

# dp 테이블(1로 초기화)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]: # 현재 요소가 더 크다면
            dp[i] = max(dp[i], dp[j] + 1) # 새로운 긴 수열 길이 갱신

print(max(dp))

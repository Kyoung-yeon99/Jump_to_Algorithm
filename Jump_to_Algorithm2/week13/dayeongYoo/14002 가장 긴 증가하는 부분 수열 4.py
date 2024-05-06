# 수열 a의 가장 긴 증가하는 부분 수열
# https://velog.io/@kimdukbae/BOJ-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-Python

# 수열 크기
n = int(input())
# 수열 a
a = list(map(int, input().split()))

# dp 테이블(1로 초기화)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:  # 현재 요소가 더 크다면
            dp[i] = max(dp[i], dp[j] + 1)  # 새로운 긴 수열 길이 갱신

print(max(dp))

# 가장 긴 증가하는 부분 수열 길이
dp_max = max(dp)
max_idx = dp.index(dp_max)
ans = list()
# dp_max == max_idx 라면 가장 긴 증가하는 부분 수열에 해당하는 수 -> 정답 리스트에 추가해줌
while max_idx >= 0:
    if dp[max_idx] == dp_max:
        ans.append(a[max_idx])
        # max_idx, dp_max 값 -1
        dp_max -= 1  # LIS 길이 -1
    max_idx -= 1
print(*reversed(ans))

n = int(input())  # 1 <= N <= 1000
a = list(map(int, input().split()))  # 1 ≤ Ai ≤ 1,000
dp = [1] * n  # a[i]를 마지막 값(가장 큰 값)으로 가지는 가장 긴 부분수열 길이. 디폴트값 1

for i in range(n):
    for j in range(i):  # i 앞의 모든 원소를 탐색
        if a[i] > a[j]:  # 증가하는 수열일 때
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))



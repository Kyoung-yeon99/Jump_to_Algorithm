# 가장 긴 증가하는 부분 수열 (LIS)

n=int(input())
arr=list(map(int,input().split()))

# i를 마지막 원소로 가지는 가장 긴 부분 수열의 길이
dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[j]+1, dp[i])

print(max(dp))
# 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수
import sys

input = sys.stdin.readline
N = int(input())
line = []
for _ in range(N):
    line.append(int(input()))

dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j]+1) # i번째 수가 가장 큰 수인 오름차순인 부분 수열의 길이 갱신

print(N - max(dp))
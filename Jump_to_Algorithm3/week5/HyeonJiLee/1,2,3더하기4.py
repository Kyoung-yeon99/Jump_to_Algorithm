# N = 1 ; 1 -> 1
# N = 2 ; 1 + 1, 2 -> 2
# N = 3 ; 1 + 1 + 1, 2 + 1, 3 -> 3
# N = 4 ; 1 + 1 + 1 + 1, 2 + 1 + 1, 3 + 1, 2 + 2 -> 4
# N = 5 ; 1 + 1 + 1 + 1 + 1, 2 + 1 + 1 + 1, 3 + 1 + 1, 2 + 2 + 1, 3 + 2 -> 5

from sys import stdin
T = int(stdin.readline().rstrip())
N = 10001
dp = [0] * N
dp[0] = 1
# 순서 없이 1, 2, 3을 사용하는 조합을 구함
for num in [1, 2, 3]:  # 각 숫자를 순서대로 추가
    for i in range(num, N):
        dp[i] += dp[i - num]

for _ in range(T):
    n = int(stdin.readline().rstrip())
    print(dp[n])

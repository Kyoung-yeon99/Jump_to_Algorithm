# 포도주 시식
# 포도주 잔 개수 n
n = int(input())
# 최대로 마실 수 있는 포도주의 양?
wine = []
for _ in range(n):
    wine.append(int(input()))

wine.insert(0, 0)  # 1-indexed -> 없으면 for문에서 index-error

# dp 테이블 생성
dp = [[0] * (n + 1) for i in range(3)]

# dp 테이블 갱신
for j in range(1, n + 1):
    # 0번째 연속 포도잔
    dp[0][j] = max(dp[0][j - 1], dp[1][j - 1], dp[2][j - 1])
    dp[1][j] = dp[0][j - 1] + wine[j]
    dp[2][j] = dp[1][j - 1] + wine[j]
    # print(dp)
# 26% 에서 실패
# print(max(dp[2]))

# 마지막 포도잔일때 각 행에서의 최댓값을 출력해야 함
print(max(dp[0][n],dp[1][n], dp[2][n]))

# N = int(input())
# wines = [0] + [int(input()) for _ in range(N)] + [0]
#
# dp = [0] * (N + 2)
#
# # 1, 2일 경우 최댓값은 연속으로 마신 경우임(초기값 지정)
# dp[1] = wines[1]
# dp[2] = dp[1] + wines[2]
#
# # dp 갱신
# for i in range(3, N + 1):
#     dp[i] = max(dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i], dp[i - 1])
# print(dp[N])

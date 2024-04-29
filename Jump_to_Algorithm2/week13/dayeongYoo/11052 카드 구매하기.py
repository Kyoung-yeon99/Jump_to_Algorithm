# 카드 개수
n = int(input())
# 카드
card = list(map(int, input().split()))
card.insert(0, 0)

# dp 테이블 생성 및 초기화
dp = [0 for _ in range(n + 1)]

# 카드 n개를 갖기 위해 지불해야하는 금액의 최댓값 갱신
# dp[0]은 0
# 1부터 dp 테이블 시작
for i in range(1, n + 1):
    for j in range(1, i + 1):  # j는 1부터 i까지 증가
        dp[i] = max(dp[i], card[j] + dp[i - j])  # j값에 따른 max값

print(dp[n])

# https://jyeonnyang2.tistory.com/m/56
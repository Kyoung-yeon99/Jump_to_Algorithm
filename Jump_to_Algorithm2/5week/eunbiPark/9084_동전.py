# 주어진 금약을 만드는 모든 방법의 수 세기

# 5원 10원으로 20원 만들기
## 20 = 10 + 10 = (5 + 5) + (5 + 5)


t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money + 1)
    dp[0] = 1

    # 동전 종류를 돌아가며
    for coin in coins:
        # 모든 경우의 수 계산
        for i in range(money + 1):
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[money])


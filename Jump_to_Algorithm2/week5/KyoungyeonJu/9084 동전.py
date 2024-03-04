tc = int(input())
for _ in range(tc):
	n = int(input())  # 동전 가지 수 1 ≤ N ≤ 20
	coins = list(map(int, input().split()))  # 정수로서 1원부터 10000원
	m = int(input())  # 만들어야 할 금액 1 ≤ M ≤ 10000
	dp = [0]*(m+1)
	dp[0] = 1
	# bottom-up
	for coin in coins:  # 각 동전이 만들 수 있는 금액 테이블 갱신
		for i in range(coin, m+1):  # 각 동전의 값부터 끝까지
			dp[i] += dp[i-coin]  # 원래 저장된 값에서 새로운 동전이 만들 수 있는 방법 더하기

	print(dp[-1])


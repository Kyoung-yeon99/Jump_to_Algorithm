# 화폐단위
# 1, 5, 10, 50, 100, 500원
# 정수 금액 만들기
# 30원: 1원*30개, 10원*2개+5원*2

tc = int(input())

for t in range(tc):
    n = int(input())
    coin = list(map(int, input().split()))
    coin.insert(0, 0)  # 0번째 인덱스에 0을 삽입
    money = int(input())

    # cache
    # 2차원 배열 생성
    cache = [[0] * (money + 1) for _ in range(n + 1)]
    # 0으로 만드는 경우의 수는 1가지
    for i in range(n + 1):
        cache[i][0] = 1
    # 2차원 배열 채우기
    for i in range(1, n + 1):
        for j in range(1, money + 1):
            cache[i][j] = cache[i - 1][j]

            if j - coin[i] >= 0:  # 음수는 계산하지 않음
                cache[i][j] += cache[i][j - coin[i]] # 현재 값: n-자기 코인값

    print(cache[n][money])

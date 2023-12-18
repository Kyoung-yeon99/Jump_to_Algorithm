money = int(input())
stock = list(map(int, input().split()))

# 준현 - 가능한 만큼 많이 매수
def bnp(money, stock):
    bnp_cnt = 0
    for s in stock:
        # 매수 가능하면 - 전량 매수
        if money // s > 0:
            bnp_cnt += money // s
            money = money % s

    return money + bnp_cnt * stock[-1]


# 성민 - 3일 연속 상승 -> 전량 매도, 3일 연속 하락 -> 전량 매수
def timing(money, stock):
    timing_cnt = 0
    # 3일 연속
    for i in range(3, len(stock)):
        # 상승
        # stock[i-3] > stock[i-2] > stock[i-1] > stock[i]
        if stock[i - 2] - stock[i - 3] > 0 and stock[i - 1] - stock[i - 2] > 0 and stock[i] - stock[i - 1] > 0:
            # 전량 매도
            # print('전량 매도: ', i + 1, '주식 개수: ', timing_cnt)
            money += timing_cnt * stock[i]
            timing_cnt = 0

        # 하강
        # stock[i-3] < stock[i-2] < stock[i-1] < stock[i]
        if stock[i - 2] - stock[i - 3] < 0 and stock[i - 1] - stock[i - 2] < 0 and stock[i] - stock[i - 1] < 0:
            # 전량 매수
            # print('전량 매수일: ', i + 1, '현재 주식 개수: ', timing_cnt)
            # print('money: ', money, '주식 가격: ', stock[i])
            if money // stock[i] > 0:
                timing_cnt += money // stock[i]
                money %= stock[i]

    return money + timing_cnt * stock[-1]


# main
bnp_ret = bnp(money, stock)
timing_ret = timing(money, stock)
if bnp_ret > timing_ret:
    print('BNP')
elif bnp_ret < timing_ret:
    print('TIMING')
else:
    print('SAMESAME')
# 현금
m = int(input())
# 주가(1/1 ~ 1/14)
stocks = list(map(int, input().split()))

# bnp
bnp_m = m  # 지역변수화
bnp = 0  # 매수 주식
for stock in stocks:
    if stock <= m:
        bnp += bnp_m // stock
        bnp_m %= stock  # 주식 사고 남은 잔돈
# timing
timing_m = m
timing = 0
for i in range(len(stocks) - 3):
    if stocks[i] > stocks[i + 1] > stocks[i + 2]:  # 현재 주식: 상승
        timing += timing_m // stocks[i + 3]  # 매도
        timing_m %= stocks[i + 3]
    elif stocks[i] < stocks[i + 1] < stocks[i + 2]:  # 현재 주식: 하락
        timing_m += timing * stocks[i + 3]  # 매수
        timing = 0

bnp_res = [bnp_m + (stocks[-1] * bnp)]
timing_res = [timing_m + (stocks[-1] * timing)]

if bnp_res > timing_res:
    print('BNP')
elif timing_res > bnp_res:
    print('TIMING')
else:
    print('SAMESAME')

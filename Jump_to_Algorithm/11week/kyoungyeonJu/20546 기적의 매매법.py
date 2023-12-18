seed = int(input())
price = list(map(int, input().split()))
jh, sm = seed, seed  # 보유 현금
jh_cnt, sm_cnt = 0, 0  # 보유 주식 수

for i in range(len(price)-1):
    if jh >= price[i]:
        jh_cnt += jh//price[i]
        jh -= price[i]*jh_cnt

for i in range(2, len(price)-1):
    # 보유한 주식이 있고 3일 연속 상승하면
    if sm_cnt > 0 and price[i-3] < price[i-2] < price[i-1] < price[i]:
        sm += sm_cnt*price[i]
        sm_cnt = 0
    # 보유한 현금이 주식 가격 이상이고 3일 연속 하락하면
    if sm >= price[i] and price[i-3] > price[i-2] > price[i-1] > price[i]:
        sm_cnt += sm//price[i]
        sm -= price[i]*(sm//price[i])

jh += jh_cnt*price[-1]
sm += sm_cnt*price[-1]

if jh > sm:
    print("BNP")
elif jh < sm:
    print("TIMING")
else:
    print("SAMESAME")


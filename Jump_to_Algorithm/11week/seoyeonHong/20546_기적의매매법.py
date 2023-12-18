cash = int(input()) # 초기 자금
stock = list(map(int, input().split())) # 주가
jc, sc = cash, cash # 준형, 성민의 현금 자산
jb, sb = 0, 0 # 준형, 성민의 주식 수

for i in range(14):
    jb += jc // stock[i] # 전량 매수
    jc = jc % stock[i] # 주식 매수 후 남은 현금
    
    if(i > 2):
        # 3일 연속 상승 시 전량 매도
        if sb > 0 and stock[i-3] < stock[i-2] and stock[i-2] < stock[i-1]:
            sc = sc + sb * stock[i]
            sb = 0
        # 3일 연속 하락 시 전량 매수
        elif sc >= stock[i] and stock[i-3] > stock[i-2] and stock[i-2] > stock[i-1]:
            sb += sc // stock[i]
            sc = sc % stock[i]

bnp = jc + jb * stock[-1]
timing = sc + sb * stock[-1]

if bnp > timing:
    print("BNP")
elif bnp == timing:
    print("SAMESAME")
else:
    print("TIMING")



T = int(input())
if T % 10 != 0: # 300초(5분), 60초(1분), 10초 모두 10의 배수임을 이용
    print(-1)
else:
    a, b, c = 0, 0, 0 # 버튼 A, B, C를 누르는 횟수
    if T / 300 >= 1 :  
        a = T // 300
        T = T % 300
    if T / 60 >= 1 :
        b = T / 60
        T = T % 60
    if T / 10 >= 1 :
        c = T / 10
    print("%d %d %d" % (a, b, c))
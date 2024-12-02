# 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램
N = int(input())
cnt = 1
n = 1
for i in range(N//6+1): # 숫자가 6*i만큼 커질수록 지나가야 하는 방의 개수가 늘어난다
    n += 6 * i 
    if n >= N:
        break
    cnt += 1

print(cnt)
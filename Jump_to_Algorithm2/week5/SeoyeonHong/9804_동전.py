# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법의 수
import sys

input = sys.stdin.readline
T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    N = int(input()) # 동전의 가지 수
    coins = list(map(int, input().split())) # 동전의 각 금액(오름차순)
    M = int(input()) # 만들어야 할 금액

    dp = [0] * (M+1) # dp[i] -> i를 만드는 방법의 수
    dp[0] = 1    

    for coin in coins: # 작은 동전부터
        for i in range(coin, M+1): # 동전의 금액 ~ M 까지의 금액의 만드는 방법의 수 계산
            dp[i] += dp[i - coin] # i를 만드는 방법의 수는 i에서 동전의 금액을 뺀 만큼의 금액을 만드는 방법의 수와 같음
    
    print(dp[M])
    


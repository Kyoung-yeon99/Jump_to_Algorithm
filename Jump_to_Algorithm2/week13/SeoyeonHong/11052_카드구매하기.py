# N개의 카드를 구매하기 위해 지불해야 하는 금액의 최댓값
N = int(input()) # 구매하려고 하는 카드 개수
P = [0]
P.extend(list(map(int, input().split()))) # P[i] = 카드가 i개 포함된 카드팩의 가격
dp = [0 for _ in range(N+1)]
max_cost = [0 for _ in range(N+1)] # max_cost[i] = i개의 카드 금액의 최댓값

for i in range(1, N+1):
    max_cost[i] = P[i] # i개가 들어있는 카드팩의 금액으로 초기화

for i in range(2, N+1): # 2~N개를 구매했을 때 금액의 최댓값을 순서대로 갱신
    for j in range(1, i // 2 + 1):
        max_cost[i] = max(max_cost[i], max_cost[j] + max_cost[i-j])

print(max_cost[N])

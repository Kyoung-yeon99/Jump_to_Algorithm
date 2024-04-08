# 제일 오른쪽 도시로 이동하는 최소의 비용
N = int(input()) # 도시의 개수
load = list(map(int, input().split())) # 도로의 길이
cost = list(map(int, input().split())) # 주유소의 리터당 가격
total_load = sum(load) # 총 이동 거리
min_cost = 1000000000 * total_load + 1 # 최소 비용, 최대 비용으로 초기화

# 기름값이 최소인 도시에서 최대한 주유하기
# 현재 도시보다 가격이 높은 도시에서는 주유하지 X

def move(index, total_cost): # 이동
    global min_cost
    if index == N-1: # 도착했을 경우
        min_cost = min(min_cost, total_cost) # 최소 비용 갱신
        return
    
    if cost[index] == min(cost[index:-1]): # 남은 도시들 중 기름값이 가장 싸다면
        total_cost += cost[index] * sum(load[index:]) # 남은 도로 길이만큼 주유
        min_cost = min(min_cost, total_cost) # 최소 비용 갱신
        return
        
    for i in range(index+1, N-1):
        if cost[index] > cost[i]: # 현재 도시보다 기름값이 싼 도시라면
            total_cost += cost[index] * sum(load[index:i])
            move(index+i, total_cost)
            break
            

move(0, 0)
print(min_cost)
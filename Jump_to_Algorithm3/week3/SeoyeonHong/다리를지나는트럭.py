# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    n = len(truck_weights)
    cnt = 0 # 다리를 건넌 트럭의 개수
    total_weight = 0 # 다리 위 트럭의 총 무게
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 위에 있는 트럭
    idx = 0 # 대기중인 다음 트럭 인덱스
    
    while cnt < n: # 모든 트럭이 다리를 건널 때 까지
        bridge.rotate(-1) # 하나씩 이동
        if bridge[0] != 0: # 다리를 건넜다면
            total_weight -= bridge[0]
            bridge[0] = 0
            cnt += 1 
        
        if idx < n: # 대기중인 트럭이 남았다면
            t = truck_weights[idx]
            if t <= weight - total_weight: # 트럭의 무게를 다리가 견딜 수 있다면
                bridge[0] = t
                total_weight += t
                idx += 1
        time += 1 # 시간 경과
    return time
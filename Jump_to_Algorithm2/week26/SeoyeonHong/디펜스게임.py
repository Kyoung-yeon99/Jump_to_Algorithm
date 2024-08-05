# https://school.programmers.co.kr/learn/courses/30/lessons/142085

# 최대 몇 라운드까지 할 수 있는지
import heapq

def solution(n, k, enemy):
    total_enemy = sum(enemy)
    total_round = len(enemy)    
    
    # 병사의 수가 적의 수보다 많거나 무적권의 횟수가 라운드 수보다 많다면 모두 막을 수 있음
    if n >= total_enemy or k >= total_round:
        return total_round

    q = [] # 최소 힙

    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            last = heapq.heappop(q)
            if last > n: # 게임 종료
                return i
            n -= last # 병사 수 차감
    return len(enemy) # 모두 방어 했을 경우
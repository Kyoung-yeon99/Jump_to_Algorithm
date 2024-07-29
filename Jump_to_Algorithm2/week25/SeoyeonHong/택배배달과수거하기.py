# https://school.programmers.co.kr/learn/courses/30/lessons/150369

# 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
def solution(cap, n, deliveries, pickups):  
    deliveries = deliveries[::-1]  
    pickups = pickups[::-1]  
    answer = 0  

    d = 0  
    p = 0  

    for i in range(n):  
        d += deliveries[i]  
        p += pickups[i]  

        while d > 0 or p > 0:  
            d -= cap  
            p -= cap  
            answer += (n - i) * 2  
    return answer
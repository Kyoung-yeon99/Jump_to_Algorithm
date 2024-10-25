# https://school.programmers.co.kr/learn/courses/30/lessons/42626#

# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
import heapq

def solution(scoville, K):
    cnt = 0 # 음식을 섞은 횟수
    n = len(scoville) # 음식의 개수
    heapq.heapify(scoville)

    for _ in range(n-1): # 음식을 섞을 수 있는 최대 횟수: n-1
        s1 = heapq.heappop(scoville) # 최솟값
        if s1 < K: # 최솟값이 K 미만일 경우
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1 + s2 * 2) # 음식 섞기
            cnt += 1
        else: # 모든값이 K 이상일 경우
            break
    return -1 if heapq.heappop(scoville) < K else cnt # 모두 K 이상인지 확인, 결과 반환
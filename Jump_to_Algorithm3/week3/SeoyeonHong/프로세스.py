# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 프로세스가 몇 번째로 실행되는지
from collections import deque
import heapq

def solution(priorities, location):
    cnt = 0 # 실행한 프로세스 개수
    q = deque([i for i in range(len(priorities))]) # 실행 대기 큐, 프로세스의 인덱스를 요소로 가짐
    pq = [-p for p in priorities]
    heapq.heapify(pq) # 최대 힙
    
    while q:
        hp = -heapq.heappop(pq) # 최대 우선순위
        while True:
            if priorities[q[0]] == hp: # 최대 우선순위일 경우
                p = q.popleft()
                cnt += 1
                if p == location: # 몇 번째로 실행되는지 알고싶은 프로세스일 경우
                    return cnt # 몇번째로 실행되었는지 반환
                break
            else:
                q.rotate(-1) # 꺼낸 프로세스를 다시 큐에 넣기
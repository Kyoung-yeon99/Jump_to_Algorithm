from collections import deque

cases = int(input())

for case in range(cases):
    n, m = map(int, input().split())
    target = m # 몇 번째로 인쇄되었는지 궁금한 문서의 위치(인덱스)
    count = 0 # 인쇄된 문서의 개수
    priorities = deque(map(int, input().split()))
    
    while priorities:
        if priorities[0] >= max(priorities): # 가장 앞에 있는 문서의 중요도가 높을 경우
            count += 1
            if target == 0: # m번째 문서가 출력될 경우
                print(count)
                break
            else:
                priorities.popleft() # 문서 출력(큐에서 제거)
                target -= 1
        else: # 가장 앞에 있는 문서의 중요도가 낮을 경우
            target = (target - 1) % len(priorities)
            priorities.rotate(-1)
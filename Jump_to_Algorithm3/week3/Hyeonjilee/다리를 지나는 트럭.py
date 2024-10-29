from collections import deque
def solution(bl, w, tws):
    bq = deque([0 for _ in range(bl)] ) # 다리 위 트럭 큐 (전체 트럭 개수만큼 0으로 초기화)
    tws = deque(tws)
    
    sum_bq = sum(bq)
    t = 1
    while sum_bq>0 or len(tws)>0:  # 대기중인 트럭 큐와 다리 위 트럭 큐가 모두 비어있으면 종료
        truck = bq.popleft() # 앞으로 한 칸 이동
        sum_bq -= truck #다리 위 트럭 무게 업데이트
        bq.append(0)  # 더미 값(0) 추가해서 bq 개수 맞추기
        if len(tws) > 0 and (tws[0] + sum_bq) <= w and len(bq) < bl + 1:  # 대기중인 트럭이 있고, 다리위 트럭들 + 현재 꺼낼 트럭 무게를 견딜 수 있고, 트럭이 올라갈 수 있으면
            bq[-1]=tws.popleft()  # 트럭 꺼내고 트럭을 다리 위에 올리기
            sum_bq+=bq[-1] #다리 위 트럭 무게 업데이트
        # print(t,':',bq,tws, sum_bq, len(tws))

        if sum_bq==0 and len(tws)==0:
            return t

        t += 1
    return t

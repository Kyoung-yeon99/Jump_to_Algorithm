def solution(p, l):
    pnum = 0
    while p: #큐가 빌 때 까지
        pc = p.pop(0) #큐에서 하나 꺼냄
        if len(p)>0 and pc < max(p): #큐에 현재 꺼낸 프로세스 우선순위보다 높은 프로세스가 있을 경우
            p.append(pc) #다시 넣기
            if l == 0 : #꺼냈던 프로세스가 구하려던 프로세스였다면
                l=len(p)-1 #프로세스 위치 업데이트
            else: #다른 프로세스라면
                l-=1 #앞으로 한 칸 이동
        else: #꺼낸 프로세스를 실행할 수 있으면
            pnum+=1
            if l==0:#꺼냈던 프로세스가 구하려던 프로세스였다면
                return pnum
            else:#다른 프로세스라면
                l-=1 #앞으로 한 칸 이동
    return pnum

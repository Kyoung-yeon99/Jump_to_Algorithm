# 각 배포마다 몇 개의 기능이 배포되는지
def solution(progresses, speeds):
    answer = [] # 각 배포마다 포함된 기능의 개수
    n = len(progresses) # 기능의 개수
    completed = [False for _ in range(n)] # 개발 완료 여부
    released = [False for _ in range(n)] # 배포 여부
    
    while False in released: # 모든 기능이 배포될 때까지
        for i in range(n): # 각 기능에 대해
            if not completed[i]:
                progresses[i] += speeds[i] # 진도율 증가
                if progresses[i] >= 100:
                    completed[i] = True # 개발 완료
        r = 0 # 배포한 기능의 개수
        for j in range(n):
            if completed[j]: # 완료되었고
                if not released[j]: # 아직 배포되지 않았다면 배포
                    r += 1
                    released[j] = True
            else: # 완료되지 않았을 경우 뒤에 있는 기능들도 배포될 수 없으므로 종료
                break
        if r > 0: # 배포했을 경우
            answer.append(r) # 배포한 기능의 개수 추가
    return answer
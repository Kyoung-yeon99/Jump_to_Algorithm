def solution(p, s):
    answer=[] 
    while p: #기능 리스트가 빌때까지
        p = list(map(lambda x,y : x+y, p,s)) #각 기능 진도율 더하기
        # print(p,s)
        #배포할 기능이 있는지 맨 앞기능 진도율만 확인
        publish_num = 0 #배포시 기능의 수
        if p[0]>=100 :#배포해야하는 경우
            while len(p)>0 and p[0] >=100: #진도율 100이상만 pop
                p.pop(0)
                s.pop(0) #speed 도 같이 pop
                publish_num+=1 #기능 수 세기
            answer.append(publish_num)
                      
    return answer

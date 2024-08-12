# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []
    cur = k
    next = 0
    arr = [cur] # 우박수열
    integral = [] # integral[i] : x=i ~ x= i+1 정적분값

    while cur != 1:
        if cur % 2 == 0: # 짝수
            next = cur // 2
        else: # 홀수
            next = cur * 3 + 1
        arr.append(next)
        integral.append((cur + next) / 2) # 정적분 값 계산
        cur = next
        
    for range in ranges:
        start, end = range
        end = len(arr) + end - 1
        if start < end:
            answer.append(sum(integral[start:end]))
        elif start > end: # 유효하지 않은 구간일 경우
            answer.append(-1)
        else: # 시작과 끝이 같을 경우
            answer.append(0)
    
    return answer
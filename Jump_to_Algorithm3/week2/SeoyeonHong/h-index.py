# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    n = len(citations) # 논문의 수
    h = 0
    citations.sort() # 오름차순 정렬
    for i in range(n+1):
        for j in range(n):
            # i번 이상 인용된 논문이 i편 이상이고 나머지 논문이 i번 이하 인용되었을 경우
            if citations[j] >= i and j <= i <= n-j:
                h = i  
    return h
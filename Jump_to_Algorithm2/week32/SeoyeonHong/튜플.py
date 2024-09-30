# https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=python3

# 집합 -> 튜플(배열, 중복되는 원소X)
def solution(s):
    answer = []
    sets = s[2:-2].split('},{') # 부분집합 문자열 추출
    n = len(sets) # 튜플의 길이
    
    for i in range(n):
        sets[i] = list(map(int, (sets[i].split(',')))) # 부분집합 문자열을 숫자 배열로 변환
    
    sets.sort(key = lambda set: len(set)) # 길이순으로 부분집합 정렬
    
    sets.insert(0, []) # 차집합을 구하기 위해 빈 배열 추가
    for i in range(1, n+1):
        for e in sets[i]:
            if e not in sets[i-1]:
                answer.append(e) # ai일 경우 튜플에 추가
                break
    
    return answer
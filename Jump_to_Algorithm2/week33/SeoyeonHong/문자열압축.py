# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이
def compress(l): 
    result = ''
    l.append('') # 마지막 원소의 비교로 인해 빈 문자열 추가
    i = 0
    while i < len(l) - 1:
        if l[i] == l[i+1]: # 연속되는 문자열이 같을 경우
            cnt = 1
            while i < len(l) - 1 and l[i] == l[i+1]: # 연속되는 문자열의 개수 세기
                cnt += 1
                i += 1
            result += str(cnt) + l[i] # 압축한 문자열 붙여주기
        else: # 압축되지 않는 문자열은 그대로 붙여주기
            result += l[i]
        i += 1
        
    return len(result) # 압축한 문자열의 길이 반환
    
    
def solution(s):
    N = len(s) # 원본 문자열의 길이
    min_length = N # 압축 문자열의 최소 길이
    
    for i in range(1, N//2+1):
        splitted = [] # 단위별로 나눈 문자열 리스트
        for j in range(0, N//i+1):
            part = s[i*j:i*(j+1)]
            if part: # 빈 문자열이 아닐 경우 추가
                splitted.append(part)
        min_length = min(min_length, compress(splitted)) # 최솟값 갱신
        
    return min_length
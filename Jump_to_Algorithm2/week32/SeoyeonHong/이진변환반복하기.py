# https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3

def solution(s):
    zero, count = 0, 0
    while s != '1': # s가 '1'이 될 때까지 이진 변환
        ns = '' # 0을 제거한 새로운 문자열
        for num in s:
            if num == '1':
                ns += '1'
            else:
                zero += 1 # 0의 개수 +1
        s = bin(len(ns))[2:] # 문자열의 길이를 이진법으로 표현한 문자열
        count += 1 # 이진 변환 횟수 +1
    
    return [count, zero]
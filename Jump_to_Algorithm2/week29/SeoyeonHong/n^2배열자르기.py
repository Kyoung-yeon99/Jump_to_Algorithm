# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    arr = []
    for i in range(left, right + 1):
        mod = (i + 1) % n # i + 1 번째 숫자에 대해 
        min_num = (i + 1) // n + 1 # 첫번째 배열의 몇번째 행인지 계산 -> 최소 숫자 계산
        if mod == 0:
            arr.append(n) # n번째 숫자는 무조건 n
        else:
            arr.append(max(min_num, mod))
    
    return arr
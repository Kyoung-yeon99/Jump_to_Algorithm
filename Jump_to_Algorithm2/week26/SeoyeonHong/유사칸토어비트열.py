# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def solution(n, l, r):
    answer = 0
    for i in range(l-1, r):
        answer += is_one(i)
    return answer

def is_one(d):
    if d % 5 == 2: # 반복되는 패턴의 가운데 부분일 경우 0
        return 0
    elif d < 5: # '11011' 중 0이 아닌 경우
        return 1
    return is_one(d // 5) # 5의 n승 만큼 패턴이 반복되므로 5로 나눈 나머지를 매개변수로 재귀호출
        
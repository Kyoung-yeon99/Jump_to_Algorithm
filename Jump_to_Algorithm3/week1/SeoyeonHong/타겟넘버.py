# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    max_num = sum(numbers)
    if max_num < target or target < -max_num: # 만들 수 없는 숫자일 경우
        return 0
    
    a = [0]
    for number in numbers:
        b = []
        for n in a:
            b.append(n + number) # 더할 경우
            b.append(n - number) # 뺄 경우
        a = b

    return a.count(target)
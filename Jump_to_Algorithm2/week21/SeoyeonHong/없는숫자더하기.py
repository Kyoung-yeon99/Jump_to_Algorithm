# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    sum = 0
    for i in range(1, 10):
        if i not in numbers:
            sum += i
    return sum 
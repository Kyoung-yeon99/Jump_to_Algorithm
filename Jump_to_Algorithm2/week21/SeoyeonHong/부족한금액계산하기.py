# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    lack = price * (count + 1) * count / 2 - money
    return lack if lack > 0 else 0
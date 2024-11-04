# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, n): # 10진수를 n진수로 변환
    number = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if n == 10:
        return num
    
    result, r = '', 0
    while True:
        r = num % n
        num //= n
        result += number[r]
        if num == 0:
            break
            
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    numbers = ''
    
    for num in range(t * m):
        numbers += convert(num, n)
        if len(numbers) > p-1 + (t-1) * m:
            break
            
    idx = p - 1
    for i in range(t): # 순서 p에 해당하는 숫자 구하기
        answer += numbers[idx]
        idx += m
        
    return answer
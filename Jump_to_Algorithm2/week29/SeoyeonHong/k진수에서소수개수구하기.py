# https://school.programmers.co.kr/learn/courses/30/lessons/92335

# n을 k진수로 변환한 수 안에 조건을 만족하는 소수의 개수
def is_prime(n): # 소수인지 판별
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1
    
def solution(n, k):
    answer = 0
    conv_num = ''
    # k진수로 변환한 수
    if k == 10: # 10진수일 경우 변환 X
        conv_num = str(n)
    else: # 10진수가 아닐 경우 변환
        num = n
        digit = 12
        while k ** digit > num:
            digit -= 1
        while digit > -1:
            conv_num += str(num // (k ** digit))
            num = num % (k ** digit)
            digit -= 1

    part_nums = conv_num.split('0') # 0을 기준으로 문자열 분리
    while '' in part_nums: # 공백 문자열 제거
        part_nums.remove('')
        
    for part_num in part_nums:
        answer += is_prime(int(part_num)) # 소수일 경우 +1

    return answer
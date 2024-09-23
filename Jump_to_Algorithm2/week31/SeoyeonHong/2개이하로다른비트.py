# https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3

def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0: # 홀수일 경우
            answer.append(num + 1) # 마지막 자리수를 0에서 1로 변환한 수
        else: # 짝수일 경우
            bit = '0' + bin(num)[2:] # 이진수로 변환
            diff_bit = list(bit) # 2개 이하로 다른 비트
            idx = bit.rfind('0') # 가장 오른쪽에 위치하는 0의 인덱스
            diff_bit[idx] = '1' # num보다 큰 수로 만들기 위해 '10'으로 변환
            diff_bit[idx+1] = '0'
            answer.append(int(''.join(diff_bit), 2))
    return answer

# 이진수 십진수 변환 구현한 풀이
# def solution(numbers):
#     answer = []
    
#     def to_binary(d): # 십진수를 이진수로 변환
#         b = ''
#         while d > 0:
#             b = str(d % 2) + b
#             d //= 2
#         return b
    
#     def to_decimal(b): # 이진수를 십진수로 변환
#         d = 0
#         hd = len(b)
#         for i in range(hd):
#             d += int(b[i]) * 2 ** (hd - i - 1)
#         return d
    
#     for num in numbers:
#         if num % 2 == 0: # 홀수일 경우
#             answer.append(num + 1)
#         else:
#             bit = '0' + to_binary(num)
#             diff_bit = list(bit)
#             idx = bit.rfind('0')
#             diff_bit[idx] = '1'
#             diff_bit[idx+1] = '0'
#             answer.append(to_decimal(''.join(diff_bit)))
#     return answer

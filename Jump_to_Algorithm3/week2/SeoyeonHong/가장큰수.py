# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 순서를 재배치하여 만들 수 있는 가장 큰 수
def solution(numbers):
    numbers = [str(num) for num in numbers] # 문자열로 바꾸기
    # 숫자는 최대 1000이므로 *3을 해서 최소 자리수 맞추어 비교, 정렬
    numbers = sorted(numbers, key= lambda x: x*3)
    new_number = ''.join(numbers[::-1]) # 새로운 숫자 문자열 생성
    return '0' if int(new_number) == 0 else new_number # 0일 경우 0 여러개로 이루어진 문자열이 되지 않도록 주의
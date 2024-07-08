# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    a = list(map(int, s.split())) # 문자열을 숫자 배열로 변환
    a = sorted(a) # 오름차순 정렬
    answer = str(a[0]) + ' ' + str(a[-1]) # 최솟값 + 공백 + 최댓값 형태의 문자열 생성
    return answer
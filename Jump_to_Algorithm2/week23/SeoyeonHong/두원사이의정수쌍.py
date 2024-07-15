# https://school.programmers.co.kr/learn/courses/30/lessons/181187

# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수
import math

def solution(r1, r2):
    answer = 0
    for x in range(r2): # 1사분면 기준
        min_y, max_y = 1, 0 # y가 0인 경우 제외
        if x < r1: # r1과 겹치는 부분이 있을 경우
            min_y = math.ceil(math.sqrt(r1 ** 2 - x ** 2)) # 최소값 설정
        max_y = int(math.sqrt(r2 ** 2 - x ** 2)) # 최댓값 설정
        answer += max_y - min_y + 1 # 점의 개수 추가
    return answer * 4 # 각 사분면이 대칭이므로 4배
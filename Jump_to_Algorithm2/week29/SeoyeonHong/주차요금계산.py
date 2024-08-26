# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math

# 자동차별 주차 요금 계산 
def solution(fees, records):
    answer = []
    total_time = defaultdict(int) # 0으로 초기화
    last_in = {}
    for record in records:
        when, car, enter = record.split()
        hour, minute = map(int, when.split(':'))
        when = hour * 60 + minute # 입/출차한 시각을 분으로 환산
        if enter == 'IN': # 입차
            last_in[car] = when
        else: # 출차
            time = when - last_in[car] # 주차 시간
            total_time[car] += time # 누적 주차 시간 갱신
            last_in[car] = -1

    for car in last_in:
        if last_in[car] >= 0: # 마지막 기록이 입차일 경우
            total_time[car] += 23 * 60 + 59 - last_in[car] # 23:59에 출차한 것으로 주차 시간 계산


    cars = sorted(last_in)

    for car in cars:
        time = total_time[car]
        time -= fees[0] # 기본 시간을 제외한 주차 시간
        answer.append(fees[1]) # 기본 요금
        if time > 0: # 기본 시간 초과
            answer[-1] += fees[3] * (math.ceil(time / fees[2])) # 추가 요금 계산

    return answer
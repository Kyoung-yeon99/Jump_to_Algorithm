# https://school.programmers.co.kr/learn/courses/30/lessons/62048

import math

def solution(w,h):
    count = 0
    
    if w == h: # 대각선의 기울기가 1일 경우
        return w * h - w 
    elif w == 1 or h == 1: # 가로 또는 세로 길이가 1일 경우
        return 0
    else:
        if w > h: # w를 h보다 작은 수로 만들기
            w, h = h, w

        for x in range(w):
            count += int(math.floor(x * h / w)) # 나누기를 먼저 할 경우 정확도가 낮아져 오답

        return count * 2 # 대각선을 기준으로 대칭이므로 2배
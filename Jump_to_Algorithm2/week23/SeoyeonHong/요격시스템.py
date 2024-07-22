# https://school.programmers.co.kr/learn/courses/30/lessons/181188

# 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값
def solution(targets):
    missile = 0 # 미사일 개수
    targets.sort(key = lambda x: x[1]) # e를 기준으로 정렬
    end = 0 # 요격한 기지의 e
    for target in targets:
        if target[0] >= end: # end보다 target의 s가 앞에 있을 경우
            missile += 1
            end = target[1] # end 재설정
    return missile
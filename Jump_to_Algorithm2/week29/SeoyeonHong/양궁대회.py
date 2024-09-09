# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    global max_diff
    global answer
    max_diff = 0
    answer = [-1]

    def shoot(left, shots, apeach, lion):
        global max_diff
        global answer

        if len(shots) == 10: # 1~10 점을 모두 쐈다면
            shots += [left] # 0점에 쏜 화살은 0개
            diff = lion - apeach # 라이언과 어피치의 점수 차
            if diff > 0 and diff >= max_diff: # 라이언이 이기고 점수차가 최고일 경우
                if max_diff == diff: # 점수차가 기존의 최고 기록과 같다면
                    for i in range(10, 0, -1): # 가장 낮은 점수를 더 많이 맞힌 경우만 갱신
                        if shots[i] > answer[i]:
                            break
                        elif shots[i] < answer[i]:
                            return
                max_diff = diff
                answer = shots
            return
        
        index = len(shots)
        score = 10 - index # 과녁의 점수
        min_shot = info[index] + 1 # 라이언이 점수를 획득하기 위해 쏴야하는 화살의 최소 개수

        if left >= min_shot: # 최소한의 화살로 점수 획득하는 경우
            shoot(left - min_shot, shots + [min_shot], apeach, lion + score)
        if min_shot > 1: # 0개를 맞혀서 어피치가 점수를 획득한느 경우
            shoot(left, shots + [0], apeach + score, lion)
        else: # 0개를 맞혀서 아무도 점수를 획득하지 않는 경우
            shoot(left, shots + [0], apeach, lion)

        return
    
    shoot(n, [], 0, 0)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    answer = 0 # 모든 공격이 끝난 직후 남은 체력, 0 이하가 될 경우 -1
    time = attacks[-1][0]
    success_time = 0 # 붕대 감기 연속 성공 시간
    current_health = health # 현재 체력
    attack_index = 0 # 공격 인덱스
    
    for t in range(time+1):
        if t == attacks[attack_index][0]: # 몬스터의 공격이 있을 경우
            success_time = 0
            current_health -= attacks[attack_index][1]
            attack_index += 1
        else: # 몬스터의 공격이 없는 경우
            if current_health != health: # 최대 체력이 아닐 경우
                success_time += 1
                recover = bandage[1]
                if success_time == bandage[0]: # 붕대 감기를 완료했을 경우
                    recover += bandage[2]
                    success_time = 0
                current_health = min(current_health + recover, health)
            else:
                success_time = 0
        if current_health <= 0: # 체력이 0 이하가 될 경우
            current_health = -1
            break

    answer = current_health
    return answer
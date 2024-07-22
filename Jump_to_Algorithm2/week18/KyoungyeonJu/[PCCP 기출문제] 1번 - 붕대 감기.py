def solution(bandage, health, attacks):
    attacks_t = [attacks[i][0] for i in range(len(attacks))]  # 공격 시간 모음
    sec = 1  # 시간 초
    bandage_t = 0  # 붕대감기 시간
    answer = health

    while sec <= attacks[-1][0]:  # 모든 공격이 진행될 때까지
        if answer <= 0:  # 체력 확인
            break

        if sec in attacks_t:  # 공격
            idx = attacks_t.index(sec)
            answer -= attacks[idx][1]
            bandage_t = 0
            # print("idx=", idx, "health=", answer)

        else:  # 붕대감기
            bandage_t += 1
            answer += bandage[1]
            if bandage_t == bandage[0]:
                answer += bandage[2]
                bandage_t = 0
            if answer > health:  # 최대 체력
                answer = health

            # print(f"health = {answer} bandage_t = {bandage_t}")

        sec += 1

    return answer if answer > 0 else -1
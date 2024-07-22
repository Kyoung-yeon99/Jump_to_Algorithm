def solution(bandage, health, attacks):
    con_time = 0  # 연속 시간
    time = 0  # 현재 시간
    idx = 0
    mx = health

    while 1:
        time += 1

        # 마지막 공격일 때
        if idx >= len(attacks):
            return health

        # 몬스터 공격 확인
        if attacks[idx][0] == time:  # 공격시간이면

            # 공격
            health -= attacks[idx][1]

            # 체력 확인
            if health <= 0:
                return -1

            con_time = 0
            idx += 1


        # 체력 증가
        else:
            health += bandage[1]
            con_time += 1

            # 연속 성공
            if con_time == bandage[0]:
                health += bandage[2]
                con_time = 0  # 연속 횟수 초기화 필요

            # 최대 체력 넘어가지 않게
            if health >= mx:
                health = mx
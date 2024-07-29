def solution(cap, n, deliveries, pickups):
    answer, deli, pick = 0, 0, 0

    for i in range(n-1, -1, -1):  # 가장 먼 곳에서 부터 배달 및 수거
        cnt = 0

        deli += deliveries[i]  # 배달할 상자 수
        pick += pickups[i]  # 수거할 상자 수

        while deli > 0 or pick > 0:  # 배달하거나 수거해야할 상자의 수가 아직 있다면
            deli -= cap  # 힌 번 배달 끝내기
            pick -= cap  # 한 번 수거 끝내기
            cnt += 1  # 배달 횟수 계산

        answer += (i+1)*2*cnt

    return answer

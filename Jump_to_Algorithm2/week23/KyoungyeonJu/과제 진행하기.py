def solution(plans):
    answer, paused = [], []

    # 시간 시간, 걸리는 시간 int로 변환
    for p in plans:
        h, s = p[1].split(':')
        h, s = int(h), int(s)
        p[1] = h * 60 + s
        p[2] = int(p[2])

    plans = sorted(plans, key=lambda x: x[1])  # plans 시작 시간 순 정렬하기

    for i in range(len(plans) - 1):
        end_time = plans[i][1] + plans[i][2]

        if end_time <= plans[i + 1][1]:  # 뒤의 과제가 시작하기 전에 끝나면
            answer.append(plans[i][0])

            while paused and end_time + paused[-1][1] <= plans[i + 1][1]:
                end_time += paused[-1][1]
                answer.append(paused[-1][0])
                paused.pop()

            # 테케4,5,6,10 과제가 끝나고 다음 과제 시작 전까지, paused의 마지막 요소의 남은 시간 줄이기
            if paused:
                a, b = paused.pop()
                paused.append([a, b - (plans[i + 1][1] - end_time)])

        else:
            left_time = end_time - plans[i + 1][1]
            paused.append([plans[i][0], left_time])

    answer.append(plans[-1][0])  # 마지막 과목 추가

    while paused:  # 남아있는 과제들 추가
        answer.append(paused.pop()[0])

    return answer


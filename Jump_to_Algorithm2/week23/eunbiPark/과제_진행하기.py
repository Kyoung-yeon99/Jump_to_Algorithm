def solution(plans):
    n = len(plans)
    ans = []
    stack = []

    # 1. sort
    plans.sort(key=lambda x: x[1])

    # 2. 분 변환
    for p in plans:
        p[1] = int(p[1][0:2]) * 60 + int(p[1][3:5])
        p[2] = int(p[2])

    # 패딩 처리 (for 문에서 i + 1 확인하기 위해서)
    plans.append(['', float("inf"), 0])

    # 3. 과제 시작

    for i in range(n):
        name, time, duration = plans[i]
        next_time = plans[i + 1][1]

        # 딱 맞게 끝냄
        if time + duration == next_time:
            ans.append(name)
        # 시간이 모자름
        elif time + duration > next_time:
            stack.append([name, 0, time + duration - next_time])
        # 시간이 남음
        else:
            # 3-1. 현재 숙제 끝내기
            ans.append(name)
            # 3-2. 이전에 못했던 것 끝내기
            now = time + duration

            while stack and now <= next_time:
                n_name, _, n_duration = stack.pop()
                # 딱맞게 끝냄
                if now + n_duration == next_time:
                    ans.append(n_name)
                    break
                # 시간이 모자름
                elif now + n_duration > next_time:
                    stack.append([n_name, 0, now + n_duration - next_time])
                    break
                # 시간이 남음
                else:
                    ans.append(n_name)
                    now += n_duration

    return ans
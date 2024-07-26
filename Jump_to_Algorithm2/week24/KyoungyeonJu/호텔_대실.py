def solution(book_time):
    # 최소 객실 구하기
    # 사용한 객실은 퇴실 + 10분 청소 후 사용 가능

    times = []  # 변환시킨 시작 시각, 종료 시각
    for i in range(len(book_time)):
        start, end = book_time[i]
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        start = int(start_h) * 60 + int(start_m)
        end = int(end_h) * 60 + int(end_m)
        times.append([start, end])

    times = sorted(times, key=lambda x: x[0])  # 시작 시각 순으로 정렬

    a = [times[0][1]]
    for i in range(1, len(times)):
        NEW_ROOM = True
        for j in range(len(a)):
            if a[j] + 10 <= times[i][0]:
                a[j] = times[i][1]
                NEW_ROOM = False
                break

        if NEW_ROOM:
            a.append(times[i][1])

    return len(a)
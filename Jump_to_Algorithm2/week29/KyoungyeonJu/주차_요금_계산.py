from collections import defaultdict
from math import ceil


def solution(fees, records):
    answer = []
    # 상태(IN or OUT) 와 시간(입차한 시간, 이미 주차된 시간)
    # 다시 입차했다면 -> 이미 주차된 시간 + 입차한 시간
    # IN이면 나가지 않은 상태로 23:59에 OUT 했다고 계산
    # OUT이면 주차된 시간 기록

    status = defaultdict()  # 상태 저장
    times = defaultdict()  # 입차한 시간, 이미 주차된 시간 저장
    for r in records:
        time, car, stat = r.split()
        h, m = time.split(":")
        t = int(h) * 60 + int(m)

        if stat == 'IN':
            status[car] = stat
            if car in times.keys():  # 이미 입차한 기록이 있는 차
                in_time, park_time = times[car]
                times[car] = (t, park_time)
            else:  # 처음 입차한 차
                times[car] = (t, 0)  # 입차한 시간, 주차된 시간

        elif stat == 'OUT':
            status[car] = stat
            in_time, park_time = times[car]
            park_time += (t - in_time)
            times[car] = (0, park_time)

    def_time, def_pay, unit_time, unit_pay = fees[0], fees[1], fees[2], fees[3]
    for car, stat in status.items():
        if stat == "IN":  # 아직 주차 중인 차
            in_time, park_time = times[car]
            park_time += (23 * 60 + 59 - in_time)
        elif stat == "OUT":
            _, park_time = times[car]

        fee = 0
        if park_time <= def_time:
            fee = def_pay
        else:
            fee = def_pay + ceil((park_time - def_time) / unit_time) * unit_pay
        answer.append((car, fee))

    answer.sort(key=lambda x: int(x[0]))

    return [money for car, money in answer]


"""
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]

"""

tcs = [
    [[180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]],
    [[120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]],
    [[1, 461, 1, 10],	["00:00 1234 IN"]]
]

for tc in tcs:
    print(solution(*tc))
    print()
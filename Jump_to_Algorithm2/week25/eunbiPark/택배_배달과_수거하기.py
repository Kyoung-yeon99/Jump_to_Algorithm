def solution(cap, n, deliveries, pickups):
    # 멀리 있는 곳들의 작업을 먼저 끝내야 함 
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    ans = 0

    delivery = 0
    pick = 0

    for i in range(n):
        delivery += deliveries[i]
        pick += pickups[i]

        while delivery > 0 or pick > 0:
            delivery -= cap
            pick -= cap
            ans += (n - i) * 2

    return ans

# 조건을 만족하도록 예산을 배정하는 프로그램
N = int(input()) # 지방의 수
requests = list(map(int, input().split())) # 각 지방의 예산요청
M = int(input()) # 총 예산

if sum(requests) <= M: # 모든 요청을 배정할 수 있다면
    print(max(requests)) # 예산요청의 최댓값 출력
else: # 모든 요청이 배정될 수 없는 경우
    l, r = M // N, max(requests) # 이분탐색을 위한 값 설정
    while l <= r:
        mid = (l + r) // 2 # 상한액
        if mid == l or mid == r:
            print(mid)
            break
        total = 0
        for request in requests:
            total += min(request, mid)
        if total < M: # 합이 총액을 넘을 경우 l 값 조정
            l = mid
        elif total > M: # 합이 총액보다 작을 경우 r 값 조정
            r = mid
        else: # 합이 총액과 같을 경우
            print(mid)
            break


    
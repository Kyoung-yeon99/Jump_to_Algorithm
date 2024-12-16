# 정해진 총액 이하에서 가능한 한 최대의 총 예산 배정 방법
# 1. 모든 요청이 배정 가능한 경우 그대로 배정
# 2. 모든 요청이 배정 불가능한 경우, 특정한 정수 상한액을 계산하여 그 이상인 요청은 모두 상한액 배정, 그 이하는 그대로 배정

n = int(input())
requested_budget = list(map(int, input().split()))
total_budget = int(input())
if sum(requested_budget) <= total_budget:
    print(max(requested_budget))
else:
    left = total_budget // n
    right = max(requested_budget)

    while left <= right:
        mid = (left+right)//2
        sum_budget = 0

        for i in requested_budget:
            sum_budget += min(i, mid)

        if sum_budget > total_budget:
            right = mid - 1
        else:
            left = mid + 1

    print(right)

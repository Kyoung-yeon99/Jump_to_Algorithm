#정해진 총액 내 가능한 한 최대의 예산
from sys import stdin
from math import ceil

N = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
total = int(stdin.readline().rstrip())

#모든 요청이 배정될 수 있는 경우
if sum(arr) <= total:
    print(max(arr))
else:
    #모든 요청이 배정될 수 없는 경우
    #예산순으로 정렬하고 남은 예산 계산하기
    arr.sort()

    for i in range(N):
        #현재 상한액 계산하기
        max_budget = total // (N - i)
        if arr[i] <= max_budget:
            #상한액 이하면 그대로 주기
            total -= arr[i]
        else:
            #상한액 넘으면 그대로 출력
            print(max_budget)
            break
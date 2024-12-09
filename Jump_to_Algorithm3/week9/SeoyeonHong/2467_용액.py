# 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램

N = int(input())
solution = list(map(int, input().split())) # 용액의 특성값, 오름차순

l, r = 0, N-1
min_value = int(1e9)
answer = []
if solution[l] > 0: # 모두 산성일 경우
    print(solution[l], solution[l+1])
elif solution[r] < 0: # 모두 알칼리성일 경우
    print(solution[r-1], solution[r])
else:
    while solution[l] < solution[r]:
        value = solution[l] + solution[r]
        if abs(value) < min_value: # 0에 가장 가까운 특성값(절댓값) 갱신
            min_value = abs(value)
            answer = [solution[l], solution[r]]
        if value == 0:
            answer = [solution[l], solution[r]]
            break
        elif value > 0:
            r -= 1
        else:
            l += 1

    print(*answer)
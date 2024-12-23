# 길이 N짜리 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 길이 구하기
# 그러한 합을 만드는 것이 불가능하면 0 출력

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = []  # 부분합이 S 이상인 경우, 부분합의 길이
partial_sum, cnt, end = 0, 0, 0

for i in range(N):
    while partial_sum < S and end < N:
        partial_sum += nums[end]
        cnt += 1
        end += 1

    if partial_sum >= S:
        answer.append(cnt)

    partial_sum -= nums[i]
    cnt -= 1

print(min(answer) if answer else 0)


"""
# 시간 초과
N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = []  # 부분합이 S 이상인 경우, 부분합의 길이
list = []  # 부분합
end = 0

for i in range(N):
    while sum(list) < S and end < N:
        list.append(nums[end])
        end += 1
    if sum(list) >= S:
        answer.append(len(list))
    list.pop(0)

print(min(answer) if answer else 0)
"""
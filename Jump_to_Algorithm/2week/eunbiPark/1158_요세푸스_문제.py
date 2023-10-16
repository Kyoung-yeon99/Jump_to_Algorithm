n, k = map(int, input().split()) # 사람 수, 제거 순서

people = [
    i for i in range(1, n + 1)
]

ret = [] # 제거한 사람 append
idx = -1

while len(ret) != n:
    idx += k
    if idx >= len(people):
        idx %= len(people)
    ret.append(people.pop(idx))
    idx -= 1

print('<', end ='')
print(*ret, sep=', ', end='') # 출력방식 참고
print('>')


# 배열을 유지하려 했음
# 이동한 곳이 이미 제거된 사람이라면 ㄱㅊ
# 근데 중간에 제거된 사람이 있다면 값이 달라짐

# while len(ret) != n:
#     # 1. 인덱스 조정 - 제거할 곳 찾아가기
#     idx += k
#     # 1-1. 원형이라 인덱스 넘어가면 앞으로
#     if idx >= len(people):
#         idx %= len(people)
#
#     # 1. 제거된 사람인지 확인
#     while people[idx] == -1:
#     # if people[idx] == -1:
#         # 넘어가기
#         idx += 1
#
#     # 2. ret 배열에 추가
#     ret.append(people[idx])
#
#     # 3. 제거
#     people[idx] = -1
#
#
# print(*ret)



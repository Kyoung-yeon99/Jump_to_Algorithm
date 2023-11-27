# 남은 것 중 가장 늦게 사용되는 것 뽑기
n, k = map(int, input().split())
use = list(map(int, input().split()))
code = []
answer = 0

for plug in range(k):
    if use[plug] in code:
        continue

    if len(code) < n:
        code.append(use[plug])
        continue

    priority = []
    for c in code: # 꽂힌 코드
        if c in use[plug:]:
            priority.append(use[plug:].index(c))
        else:
            priority.append(101)

    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(use[plug])
    answer += 1

print(answer)
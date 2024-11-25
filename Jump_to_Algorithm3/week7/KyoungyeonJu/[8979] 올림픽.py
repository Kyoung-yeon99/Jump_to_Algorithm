# 등수= (자신보다 더 잘한 나라의 수) + 1
from collections import defaultdict


n, k = map(int, input().split())
d = defaultdict(list)
answer_medals, answer = tuple(), 0

for _ in range(n):
    idx, gold, silver, bronze = map(int, input().split())
    d[(gold, silver, bronze)].append(idx)
    if idx == k:
        answer_medals = (gold, silver, bronze)

medals = list(d.keys())
medals.sort(key=lambda x: (-x[0], -x[1], -x[2]))  # 내림차순

for m in medals:
    if m == answer_medals:
        break
    answer += len(d[m])

print(answer+1)

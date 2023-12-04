# 합이 M이 넘지 않는 한도 내에서 합을 가장 크게 만들기 (3장 고르기)
# 카드의 개수 3~100 => 다 해보기

from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))

com_cards = list(combinations(cards, 3))

result  = 0
for c in com_cards:
    tmp_res = sum(c)
    if tmp_res <= m and m - result > m - tmp_res:
        result = tmp_res

print(result)
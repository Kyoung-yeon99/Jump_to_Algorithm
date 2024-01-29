from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_cnt = Counter(cards)
# Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

for num in nums:
    print(card_cnt.get(num, 0), end=" ")

# 시간초과 코드
# lst = defaultdict(int)
#
# for num in nums:
#     lst[num] = 0
#
# for num in nums:
#     for card in cards:
#         if card == num:
#             lst[num] += 1
#
# for l in lst.values():
#     print(l, end=" ")

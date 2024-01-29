n = int(input()) # 가지고 있는 숫자 카드 개수
cards = list(map(int, input().split())) # 각 숫자 카드에 적혀있는 정수
card_dict = {}

for card in cards:
    if card in card_dict:
        card_dict[card] = card_dict[card] + 1
    else:
        card_dict[card] = 1

m = int(input())
nums = list(map(int, input().split())) # m개의 정수

for num in nums:
    print(card_dict[num] if num in card_dict else 0, end=' ')


# 시간초과
# n = int(input()) # 가지고 있는 숫자 카드 개수
# card = list(map(int, input().split())) # 각 숫자 카드에 적혀있는 정수

# m = int(input())
# nums = list(map(int, input().split())) # m개의 정수

# for num in nums:
#     print(card.count(num), end=' ')
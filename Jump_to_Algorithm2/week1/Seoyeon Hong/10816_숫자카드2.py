n = int(input()) # 가지고 있는 숫자 카드 개수
cards = list(map(int, input().split())) # 각 숫자 카드에 적혀있는 정수
card_dict = {} # 숫자 카드의 개수 저장

for card in cards:
    if card in card_dict: # 이미 숫자가 key 값으로 있을 경우 기존 개수+1
        card_dict[card] = card_dict[card] + 1
    else: # 새로운 숫자일 경우 key값 생성 후 값을 1로 저장
        card_dict[card] = 1

m = int(input())
nums = list(map(int, input().split())) # m개의 정수

for num in nums: # 각 숫자에 대하여 딕셔너리에 개수가 있을 경우 해당 값 출력, 없을 경우 0 출력
    print(card_dict[num] if num in card_dict else 0, end=' ')

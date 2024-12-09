# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램
from collections import deque

N = int(input()) # 카드의 개수
card = deque([i for i in range(1, N+1)])
last_card = 0

while card:
    last_card = card.popleft() # 제일 위에 있는 카드 버리기
    card.rotate(-1) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기

print(last_card)
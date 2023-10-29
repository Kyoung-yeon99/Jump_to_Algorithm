import sys

n = int(sys.stdin.readline())
myCards = list(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는 숫자 카드
cardDict = dict()
for card in myCards: # 딕셔너리 자료구조로 변경
    cardDict[card] = True
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는지 아닌지 구해야 하는 숫자 카드

for c in cards:
    if cardDict.get(c) is not None: # key 값으로 검색
        print(1, end=' ')
    else:
        print(0, end=' ')
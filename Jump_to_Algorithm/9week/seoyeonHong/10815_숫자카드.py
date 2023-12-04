import sys
import heapq

n = int(sys.stdin.readline())
myCards = list(map(int, sys.stdin.readline().split()))
cardDict = dict()
for card in myCards:
    cardDict[card] = True
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards:
    if cardDict.get(c) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
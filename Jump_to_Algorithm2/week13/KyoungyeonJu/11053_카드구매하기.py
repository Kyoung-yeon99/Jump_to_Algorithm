import sys
input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))
cards = [0] + prices

for i in range(2, n+1):
    for j in range(i-1, i//2 -1, -1):
        sum_cards = cards[j] + cards[i-j]
        if sum_cards > cards[i]:
            cards[i] = sum_cards

print(cards[-1])
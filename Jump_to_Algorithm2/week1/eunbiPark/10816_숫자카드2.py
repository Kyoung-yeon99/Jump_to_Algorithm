from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

hash = defaultdict(int)
for c in cards:
    hash[c] += 1

for f in find:
    print(hash[f], end = ' ')
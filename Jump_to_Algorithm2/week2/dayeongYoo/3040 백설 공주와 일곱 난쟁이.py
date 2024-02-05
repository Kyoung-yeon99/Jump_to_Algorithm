from itertools import combinations

num = [int(input()) for _ in range(9)]

small = []
total = 0

pers = list(combinations(num, 7))

for per in pers:
    if sum(per) == 100:
        for p in per:
            print(p)

import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_num = 0

for i in itertools.combinations(cards, 3):
    #print(i, sum(i))
    sum_num = sum(i)
    if max_num < sum_num <= m:
        max_num = sum_num
        #print(max_num)

print(max_num)
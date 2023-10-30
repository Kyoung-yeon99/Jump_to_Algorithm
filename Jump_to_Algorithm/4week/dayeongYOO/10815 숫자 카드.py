n = int(input())
card = list(map(int, input().split()))
m = int(input())
section_numbers = list(map(int, input().split()))  # 숫자카드인지 아닌지 구할 m개의 정수

dic = {}

for s in section_numbers:
    dic[s] = 0

for c in card:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end=' ')

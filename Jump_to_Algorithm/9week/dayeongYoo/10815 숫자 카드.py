n = int(input())
cards = list(map(int, input().split()))  # n개의 숫자카드
dic = {}  # 딕셔너리 자료구조 사용
m = int(input())
nums = list(map(int, input().split()))  # m개의 정수

for num in nums:
    dic[num] = 0

for card in cards:
    if card in dic:
        dic[card] = 1 # 정수에 있다면 1로 갱신

for d in dic:
    print(dic[d], end=' ')

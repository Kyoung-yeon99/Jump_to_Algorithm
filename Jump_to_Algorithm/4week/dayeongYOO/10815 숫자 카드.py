n = int(input())
card = list(map(int, input().split()))
m = int(input())
section_numbers = list(map(int, input().split()))  # 숫자카드인지 아닌지 구할 m개의 정수

dic = {}

for s in section_numbers:  # m개의 숫자를 key로 value를 0으로 초기화
    dic[s] = 0

for c in card:  # 숫자 카드를 돌면서
    if c in dic:  # 만약 딕셔너리에 있는 수라면
        dic[c] = 1  # 해당 값의 value를 1로 바꿔준다.

for d in dic:
    print(dic[d], end=' ')  # 출력

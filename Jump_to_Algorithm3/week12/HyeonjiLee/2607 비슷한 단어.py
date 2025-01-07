from collections import Counter
N = int(input())
c = Counter(input())
answer = 0
for _ in range(N-1):
    i = input()
    item = Counter(i)

    #1. 같은 구성인지 확인
    if len(item - c) == len(c - item) == 0:
        # print(f'{i}은 같은 구성')
        answer+=1
    #2. 더하거나 빼야하는 경우
    elif abs(len(item-c) - len(c-item)) == 1 and (len(item-c) == 0 or len(c-item) == 0):
        # print(f'{i}는 하나 더하거나 빼거나')
        answer+=1
    #3. 한 문자 차이나는 경우
    elif len(item - c) == 1 and len(c - item) == 1:
        if list((item-c).values())[0] == 1 and list((c-item).values())[0] == 1 :
            # print(f'{i}은 문자 한개 차이')
            answer+=1
print(answer)
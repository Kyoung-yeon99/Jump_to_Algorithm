s = input()

dic = {0: 0, 1: 0}  # 0, 1 개수 저장
l = len(s)

for i in range(1, l):
    if s[i] != s[i - 1]:  # 0,1 바뀌는 순간
        if s[i] == '0':  # 현재 요소가 0
            dic[1] += 1

        if s[i] == '1':  # 현재 요소가 1
            dic[0] += 1

    # 마지막 숫자일경우
    if i == l - 1:
        if s[i] == '0':
            dic[0] += 1  # 자기 +1
        else:
            dic[1] += 1  # 1 덩어리 +1

print(min(dic.values())) # 최소로 뒤집는 횟수 출력

s = input()
dic = {0: 0, 1: 0}
l = len(s)

# 1. 덩어리 개수 세기
for i in range(1, l):
    if s[i] != s[i - 1]:
        if s[i] == '0':  # 현재 요소가 0이라면
            dic[1] += 1  # 그 전 덩어리는 1임.
        else:
            dic[0] += 1
    # # 마지막 덩어리도 세어줘야 함.
    if i == l - 1:
        if s[i] == '0':
            dic[0] += 1
        else:
            dic[1] += 1
# 2. 덩어리의 최솟값
print(min(dic.values()))

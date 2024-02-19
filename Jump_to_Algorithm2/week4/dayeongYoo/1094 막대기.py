# 지민이는 64cm인 막대
# 그는 길이가 Xcm인 막대가 갖고 싶어짐.
from collections import deque

# 원래 가진 막대를 더 작은 막대로 자르고, 풀로 붙여서 길이가 Xcm 막대 만드려 함.
# 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자름


x = int(input())
stick = deque([64])  # 초기 막대기 : 64
cnt = 0  # 막대기 개수 세기

while (1):
    if sum(stick) == x:
        break
    if sum(stick) - stick[0] // 2 >= x:  # 가장 짧은 걸 절반으로 자르고 합한 길이가 x보다 크다면
        stick[0] = stick[0] // 2  # 막대의 절반 중 하나를 버린다.
    else:
        stick[0] = stick[0] // 2
        stick.appendleft(stick[0])
print(len(stick))

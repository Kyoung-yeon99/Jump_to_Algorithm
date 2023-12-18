# 주파수 A에서 B로 갈 때 눌러야 하는 최소 버튼수
a, b = map(int, input().split())
n = int(input()) # 미리 지정되어 있는 주파수 개수, 1000 이하
setNum = []
for _ in range(n):
    setNum.append(int(input()))
cnt = [] # 버튼 조작 횟수

if b in setNum: # b주파수로 가는 버튼이 있을 경우
    print(1)
else:
    cnt.append(abs(a - b)) # 하나씩 증가/감소 하는 경우
    for num in setNum:
        cnt.append(abs(b - num) + 1) # num 주파수로 이동 후 하나씩 증가/감소 하는 경우
    print(min(cnt)) # 최소 버튼 조작 횟수


height = [
    int(input())
    for _ in range(9)
]

# 총 합 - (2명의 키의 합) == 100 확인
total = sum(height)

ret = []
for i in range(8):
    for j in range(i + 1, 9):
        spy = height[i] + height[j] # 난쟁이가 아닌 것 같은 2명 선택
        if total - spy == 100: # 전체 - 2명 뺀 값 == 100 이면 2명은 난쟁이가 아님
            ret.append(height[i])
            ret.append(height[j])
            break

for h in height:
    if h not in ret:
        print(h)
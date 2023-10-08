# 설탕 배달
# 점화식을 모든 화폐 단위에 대하여 차례대로 적용
weight = int(input())
sugar = [3, 5]
result = [5001] * (weight + 1)
result[0] = 0

for i in range(2):
    for j in range(sugar[i], weight + 1):
        if result[j - sugar[i]] != 5001:
            result[j] = min(result[j], result[j - sugar[i]] + 1)

if result[weight] == 5001:
    print(-1)
else:
    print(result[weight])

"""
효율적인 화폐 구성 (이것이 코딩 테스트다 p.227)
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input())) # 값 append

d = [5001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 5001:
            d[j] = min(d[j], d[j - array[i]]+1)

if d[m] == 5001:
    print(-1)
else:
    print(d[m])
"""

"""
# 과거의 내가 한 풀이... 기억X....
sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else:  # while 조건이 거짓이거나 break 문을 만나지 않은 경우 else 실행
    print(-1)
"""
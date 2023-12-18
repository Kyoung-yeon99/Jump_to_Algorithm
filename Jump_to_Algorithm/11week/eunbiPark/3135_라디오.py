a, b = map(int, input().split()) # a to b
n = int(input()) # 저장된 주파수 개수
frequency = [
    # 목표 주파수까지의 거리 저장
    abs(b - int(input()))
    for _ in range(n)
]

# 하나씩 이동하는 것 vs 저장된 곳으로 이동하고 이동하는 것
print(min(abs(a - b), min(frequency) + 1))
# a: 현재 주파수, b: 목표 주파수
a, b = map(int, input().split())
# n: 즐겨찾기 주파수 수
n = int(input())
# 즐겨찾기 버튼 list
stars = []
# 최소값
mi = float('inf')
# 즐겨찾기 버튼 list input
for _ in range(n):
    star = int(input())
    mi = min(mi, abs(star - b) + 1)  # 즐겨찾기로 누를 경우 -> 최소값 갱신

print(min(mi, abs(a - b)))  # a-b == a+b : 1번 소요됨

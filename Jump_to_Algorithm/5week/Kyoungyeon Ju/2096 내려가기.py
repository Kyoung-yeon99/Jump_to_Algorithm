import sys
input = sys.stdin.readline

n = int(input())  # 1 <=n <= 100,000
# 한 줄에는 0 이상 9 이하의 숫자가 세 개씩 존재
min_s = [0, 0, 0]
max_s = [0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().split())
    min_s = [a + min(min_s[:2]), b + min(min_s), c + min(min_s[1:])]
    max_s = [a + max(max_s[:2]), b + max(max_s), c + max(max_s[1:])]

print(max(max_s), min(min_s))

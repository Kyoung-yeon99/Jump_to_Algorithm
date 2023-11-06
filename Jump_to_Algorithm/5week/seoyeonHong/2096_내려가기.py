import sys

n = int(input())

# 메모리 초과 -> 한 줄씩만 저장하는 리스트 사용
dp_min = [0, 0, 0] 
dp_max = [0, 0, 0]
n1, n2, n3 = 0, 0, 0

for i in range(n):
    n1, n2, n3 = map(int, sys.stdin.readline().split())
    dp_min = [min(dp_min[:2]) + n1, min(dp_min) + n2, min(dp_min[1:]) + n3]
    dp_max = [max(dp_max[:2]) + n1, max(dp_max) + n2, max(dp_max[1:]) + n3]

print(max(dp_max), min(dp_min))
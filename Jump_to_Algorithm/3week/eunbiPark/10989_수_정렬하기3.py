# n = int(input())
import sys
n = int(sys.stdin.readline())
count_num = [0] * 10001

# 시초 날 것 같기도
for _ in range(n):
    # nums.append(int(input()))
    # num = int(input())
    num = int(sys.stdin.readline())
    count_num[num] += 1

for i, n in enumerate(count_num):
    if n: # 0 초과면
        for _ in range(n):
            print(i)

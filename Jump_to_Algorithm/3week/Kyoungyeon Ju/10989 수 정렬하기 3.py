# 메모리 초과 오류...
import sys

max_num = 10001
n = int(input())  # 1 ≤ N ≤ 10,000,000
arr = [0 for _ in range(max_num)]  # 인덱스 0부터 10000까지 모두 0인 리스트

for _ in range(n):
    num = int(sys.stdin.readline())  # 10,000보다 작거나 같은 자연수 1 ≤ num ≤ 10,000 그러므로 arr[0] = 0
    arr[num] += 1  # 인덱스 num, arr[num]의 값 증가


for i in range(max_num):  # 오름차순 정렬
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)


""" 
메모리 초과 
a = [int(sys.stdin.readline() for _ in range(n)]
a.sort()
for i in range(n):
    print(a[i])
"""
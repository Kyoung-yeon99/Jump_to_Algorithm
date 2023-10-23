# 시간 초과
import sys

n = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

for last in range(n-1, 1, -1):
    flag = True
    max_idx = 0
    for i in range(1, last+1):
        if arrA[i] > arrA[max_idx]:
            max_idx = i

    if last != max_idx:
        temp = arrA[max_idx]
        arrA[max_idx] = arrA[last]
        arrA[last] = temp

    for i in range(n):
        if arrA[i] != arrB[i]:
            flag = False
            break

    if flag is True:
        print(1)
        break
    
if flag is False:
    print(0)
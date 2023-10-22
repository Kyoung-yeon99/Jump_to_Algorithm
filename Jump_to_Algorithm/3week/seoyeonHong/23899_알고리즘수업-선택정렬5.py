import sys

n = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))
flag = False
countA = 0
countB = 0

if arrA == arrB or sorted(arrA) == arrB:
    print(1)
else:
    for i in range(n-1, 0, -1):
        if arrB[i] < arrB[i-1]:
            break
        else:
            countB += 1

    for last in range(n-1, 0, -1):
        max_idx = 0
        for i in range(1, last+1):
            if arrA[i] > arrA[max_idx]:
                max_idx = i
        if last != max_idx:
            temp = arrA[max_idx]
            arrA[max_idx] = arrA[last]
            arrA[last] = temp
        countA += 1
        if countA == countB:
            if arrA[:countA] == arrB[:countA]:
                print(1)
                flag = True
            break
    if flag is False:
        print(0)


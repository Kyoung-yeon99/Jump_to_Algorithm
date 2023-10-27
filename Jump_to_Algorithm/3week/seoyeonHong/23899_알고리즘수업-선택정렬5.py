import sys

n = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))
flag = False

if arrA == arrB:
    flag = True
else:
    for i in range(n-1, 0, -1):
        max_idx = arrA.index(max(arrA[:i+1]))
        if max_idx != i:
            arrA[max_idx], arrA[i] = arrA[i], arrA[max_idx]
        if arrA == arrB:
            flag = True
            break
if flag:
    print(1)
else:
    print(0)


# 시간 초과
# import sys

# n = int(sys.stdin.readline())
# arrA = list(map(int, sys.stdin.readline().split()))
# arrB = list(map(int, sys.stdin.readline().split()))
# flag = False

# for last in range(n-1, 0, -1):
#     max_idx = last
#     if arrA == arrB:
#         flag = True
#         break
#     for j in range(last):
#         if arrA[max_idx] < arrA[j]:
#             max_idx = j
#     if last != max_idx:
#         arrA[last], arrA[max_idx] = arrA[max_idx], arrA[last]
    
# if flag:
#     print(1)
# else:
#     print(0)
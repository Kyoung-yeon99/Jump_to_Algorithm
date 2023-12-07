import sys

n = int(sys.stdin.readline())
# 배열 a
a = list(map(int, sys.stdin.readline().split()))
# 배열 b
b = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1, -1, -1):
    if a == b:
        print(1)
        break
    max_idx = i

    for j in range(i - 1, -1, -1):  # range 범위 주의!!
        if a[max_idx] < a[j]:  # 최댓값 찾기
            max_idx = j

    a[i], a[max_idx] = a[max_idx], a[i]



else:
    print(0)
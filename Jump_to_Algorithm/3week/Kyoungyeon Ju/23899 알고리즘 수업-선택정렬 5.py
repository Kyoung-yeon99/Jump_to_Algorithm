def selection_sort(arr, num):
    last = num-1
    max_idx = last
    for i in range(last):
        if arr[max_idx] < arr[i]:
            max_idx = i  # 가장 큰 수의 인덱스 찾기
    arr[last], arr[max_idx] = arr[max_idx], arr[last]  # arr[last]와 가장 큰 수 교환


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
same_flag = False

while n > 0:
    if a == b:
        same_flag = True
        break
    # n 기준 selection sort
    selection_sort(a, n)
    n -= 1


if same_flag:
    print(1)
else:
    print(0)



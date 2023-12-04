n = int(input())
a = list(map(int, input().split())) # n개의 정수
m = int(input())
b = list(map(int, input().split())) # m개의 정수
a.sort() # 오름차순 정렬

def binary_search(num): # 이진 탐색
    start, end = 0, n-1
    while start <= end:
        mid = start + (end - start) // 2
        if a[mid] == num:
            return True
        elif a[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return False

for num in b:
    if binary_search(num):
        print(1)
    else:
        print(0)
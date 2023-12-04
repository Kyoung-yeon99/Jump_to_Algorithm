# 시초 주의
import sys
input = sys.stdin.readline
n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

check = {}

# 어떤 숫자 등장했는지 등록
for i in range(n):
    check[nums1[i]] = 0 # 있다고 표시

# 하나씩 확인
for j in range(m):
    if nums2[j] not in check:
        print(0, end = ' ')
    else:
        print(1, end=' ')

'''
# 이진 탐색 
for check in checks:
    low, high = 0, N-1  # cards의 이진 탐색 index
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > check:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif cards[mid] < check:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')
'''
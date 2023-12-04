import sys
input = sys.stdin.readline
# 1 ≤ N, M ≤ 500,000
# -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다


def b_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:  # 중간값과 찾는 값이 일치
            return True
        elif array[mid] > target:  # 중간값이 찾는 값보다 크면
            end = mid - 1
        else:  # 중간값이 찾는 값보다 작으면
            start = mid + 1
    return False


n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    if b_search(a, i, 0, n-1):
        print("1", end=" ")
    else:
        print("0", end=" ")


"""
import sys
input = sys.stdin.readline

n = int(input())
nc = set(map(int, input().split()))  # set이 아니라 list로 하면 시간초과
m = int(input())
mc = list(map(int, input().split()))

for value in mc:
    if value in nc:
        print(1, end=' ')
    else:
        print(0, end=' ')

"""
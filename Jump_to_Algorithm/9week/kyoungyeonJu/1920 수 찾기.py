import sys
input = sys.stdin.readline

# 1 ≤ N, M ≤ 100,000
n = int(input())
na = set((map(int, input().split())))
m = int(input())
ma = list(map(int, input().split()))
print(na)
print(ma)

for value in ma:
    if value in na:
        print("1")
    else:
        print("0")



"""
def b_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

"""
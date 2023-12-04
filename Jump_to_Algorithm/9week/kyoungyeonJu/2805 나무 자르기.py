import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 나무 수, 상근이가 원하는 나무 길이
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2
    sum_tree = 0
    for i in trees:
        if i > mid:
            sum_tree += (i - mid)
        else:
            continue
    if sum_tree >= m:  # 잘린 나무 길이 합이 원하는 길이보다 길면, 최대 높이 높이기
        start = mid+1
    else:  # 짧으면, 최대 높이 낮추기
        end = mid-1

print(end)
# 나무를 필요한 만큼만 가져가기 위한 높이의 최대값을 구하기 때문에  
# if sum_tree = m: print(m) break
# 위의 코드는 잘린 나무 길이의 합이 m와 일치하지 않으면 답을 구할 수 없다 

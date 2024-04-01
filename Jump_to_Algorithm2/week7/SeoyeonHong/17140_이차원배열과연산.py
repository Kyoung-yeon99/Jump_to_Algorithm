# A[r][c] 값이 k가 되기 위한 연산의 최소 시간
import sys

input = sys.stdin.readline
A = []
r, c, k = map(int, input().split())
r, c = r-1, c-1
for _ in range(3):
    A.append(list(map(int, input().split())))

# 최대 100번의 연산 진행
for t in range(100):
    if A[r][c] == k:
        print(t)
        exit()
    # 행의 개수 >= 열의 개수일 경우 배열 A의 모든 행에 대해서 정렬 수행
    for i in range(len(A)):
        count = {i: 0 for i in range(1, 101)}
        for num in A[i]:
            count[num] += 1
        count = sorted(count, key=lambda x : x[1])
    
    sorted_array = []
    for num in count.keys():
        if count[num] > 0:
            sorted_array.append(num)
            sorted_array.append(count[num])        
    
    # 행의 개수 < 열의 개수일 경우 모든 열에 대해서 정렬을 수행

if A[r][c] == k:
    print(100)
else:
    print(-1) # 100초가 지나도 A[r][c]가 k가 되지 않을 경우 -1 출력
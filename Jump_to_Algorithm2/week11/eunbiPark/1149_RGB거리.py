# 입력조건
import sys
N = int(sys.stdin.readline())
RGB = [0]*N
for x in range(N):
    RGB[x] = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    # 다음 RGB의 각 인덱스에 대해 이전값 중의 해당 값 제외한 RGB 중의 최솟값의 누적합
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2])+RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2])+RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1])+RGB[i][2]
print(min(RGB[N-1]))

# n = int(input())
# costs = [list(map(int, input().split())) for _ in range(n)]
#
# ret = [0] * 3
#
# for j in range(3):
# # 초깃값
# # ans = min(costs[0])
# # idx = costs[0].index(ans) # 같은 색 선택하지 않도록
#
#     ans = costs[0][j]
#     idx = j
#     print(f'j: {j}')
#     # 최솟값 선택 (이전 인덱스와 겹치지 않도록)
#     for i in range(1, n):
#         check = costs[i][:]
#         check[idx] = float('inf')
#         temp = min(check)
#         ans += temp
#         idx = check.index(temp)
#         print(f'i:{i}, idx:{idx}, temp: {temp}')
#     ret[j] = ans
#     # 처음 선정한 값이 최소가 되지 않을 수 있음
# print(ret)
# print(min(ret))



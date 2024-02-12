# 인접한 숫자간 차이의 최댓값의 최소값 - 그리디 알고리즘
import sys
from collections import deque
input = sys.stdin.readline
T = int(input()) # 테스트 케이스 개수

for _ in range(T): # 테스트 케이스마다 반복
    N = int(input()) # 숫자 개수
    L = list(map(int, input().split())) # 숫자 배열
    L = sorted(L) # 숫자 정렬
    a = deque([L.pop()]) # 최소 난이도를 가지는 숫자 배열
    d = 0 # 최소 난이도
    while L:
        n = L.pop() # 다음 위치를 가질 숫자
        l = a[0] - n
        r = a[-1] - n
        # 차이가 적은 위치에 숫자 배치, 난이도 갱신
        if l >= r:
            a.appendleft(n)
            d = max(d, l)
        else:
            a.append(n)
            d = max(d, r)
    print(d)
        

# 시간초과
# import sys
# from itertools import permutations
# input = sys.stdin.readline
# T = int(input()) # 테스트 케이스 개수

# for _ in range(T): # 테스트 케이스마다 반복
#     N = int(input()) # 통나무의 개수
#     L = list(map(int, input().split())) # 통나무의 높이
#     mind = max(L) - min(L) # 최소 난이도
    
#     for a in permutations(L, N): # 가능한 각 배열에 대해
#         a = list(a)
#         a.append(a[0]) # 처음과 마지막 통나무의 차이를 계산하기 위해 처음 통나무의 높이 추가
#         cd = 0 # 현재 배열의 난이도
#         for i in range(N):
#             cd = max(cd, abs(a[i] - a[i+1])) # 가장 큰 차이값을 난이도로 저장
#             if cd > mind: # 난이도가 지금까지의 최소 난이도보다 클 경우 더 이상 진행하지 않고 종료
#                 break
#         mind = min(mind, cd) # 최소 난이도 갱신

#     print(mind)
    


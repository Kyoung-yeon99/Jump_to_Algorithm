# 티셔츠 비용의 합을 최소로 하기
# 인접한 유치원생들의 키 차이 구하기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

child = list(map(int, input().split()))
diff = [] # 인접 원생 키 차이 등록
for i in range(n-1):
    diff.append(child[i + 1] - child[i])

diff.sort()
ret = 0
for i in range(n-k): # n-k의 키 차이를 더함
    ret += diff[i]

print(ret)
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# nCm
n, m = map(int, input().split())

'''
from itertools import combinations

combin = combinations(list(range(1, n + 1)), m)
for c in combin:
    print(*c)
'''

ret = []

def dfs(start):
    if len(ret) == m:
        print(' '.join(map(str, ret)))
        return

    for i in range(start, n + 1):
        if i not in ret:
            ret.append(i)
            dfs(i + 1)
            ret.pop()

dfs(1)
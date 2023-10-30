# 1부터 n 까지 자연수 중에서 중복 없이 m개를 고른 수열
# nPm
n, m = map(int, input().split())

ret = []

def dfs():
    if len(ret) == m:
        print(' '.join(map(str, ret)))
        return

    for i in range(1, n + 1):
        if i not in ret:
            ret.append(i)
            dfs()
            ret.pop()

dfs()


'''
from itertools import permutations

permute = permutations(list(range(1, n + 1)), m)

for p in list(permute):
    print(*p)
'''

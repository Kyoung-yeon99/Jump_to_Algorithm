# 자연수 n,m
# 1~n까지 자연수 중 중복 없이 m개를 고른 수열.
# n과 m(1) 과 차이점: 고른 수열은 오름차순이어야 함.(즉, 1 2 일때 2 1 안됨)

from itertools import combinations

n, m = map(int, input().split())
num = [x for x in range(1, n + 1)]

lst = [list(combinations(num, m))]
# 출력 조건: 숫자 간 공백, 오름차순

for ls in lst:
    for l in ls:
        print(*l)

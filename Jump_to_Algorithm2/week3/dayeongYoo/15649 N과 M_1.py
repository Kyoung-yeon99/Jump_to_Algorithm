# 자연수 n,m
# 1~n까지 자연수 중 중복 없이 m개를 고른 수열.
from itertools import combinations, permutations

n, m = map(int, input().split())
# 순서 체크-> 순열
num = [x for x in range(1, n + 1)]

lst = [list(permutations(num, m))]
# 출력 조건: 숫자 간 공백, 오름차순

for ls in lst:
    for l in ls:
        print(*l)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 (1 ≤ M ≤ N ≤ 8)
# 고른 수열은 오름차순

# combination 사용
from itertools import combinations
N, M = map(int, input().split())
nums = [str(i) for i in range(1, N+1)]
for seq in combinations(nums, M):
    print(*seq)
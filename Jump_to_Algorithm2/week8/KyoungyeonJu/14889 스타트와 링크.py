from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
teams = list(combinations([i for i in range(1, n+1)], n//2))
answer = int(1e9)

for x in range(len(teams)//2):
    sum1, sum2 = 0, 0
    t1 = combinations(teams[x], 2)
    for i, j in t1:
        sum1 += (m[i-1][j-1]+m[j-1][i-1])

    t2 = combinations(teams[len(teams)-x-1], 2)
    for i, j in t2:
        sum2 += (m[i - 1][j - 1] + m[j - 1][i - 1])

    answer = min(answer, abs(sum2-sum1))

print(answer)

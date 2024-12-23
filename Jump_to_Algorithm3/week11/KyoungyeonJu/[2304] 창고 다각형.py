import sys
input = sys.stdin.readline

n = int(input())  # 1 <= n <= 1000
heights = [0]*1001
start, end = 1000, 1
for _ in range(n):
    w, h = map(int, input().split())
    start, end = min(start, w), max(end, w)
    heights[w] = h

answer = 0
max_h = max(heights)
h = heights[start]  # 현재까지 최대 높이
for i in range(start, end):
    h = max(h, heights[i])  # 현재까지 최대 높이 갱신
    answer += min(h, max(heights[i:]))  # 현재까지 최대 높이와 앞으로 최대 높이 중 작은 것

answer += heights[end]
print(answer)

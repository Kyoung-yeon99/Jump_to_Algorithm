from collections import deque
import sys
input = sys.stdin.readline

tcs = int(input())
for i in range(tcs):
    answer = 0
    row = list(map(int, input().split()))
    heights = row[1:]
    q = deque()
    q.append(heights[0])
    for x in range(1, 20):  # 1부터 19까지
        idx = -1
        for y in range(x):  # 0부터 x-1번까지
            if q[y] > heights[x]:
                idx = y
                break
        if idx == -1:
            q.append(heights[x])
        else:
            q.insert(idx, heights[x])
            answer += (x-idx)

    print(i+1, answer)











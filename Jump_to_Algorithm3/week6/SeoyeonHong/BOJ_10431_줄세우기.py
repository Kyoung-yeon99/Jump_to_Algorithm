import sys
from collections import deque

input = sys.stdin.readline
P = int(input())

for _ in range(P):
    steps = 0
    heights = list(map(int, input().split()))
    unsorted = deque(heights[2:])
    sorted = deque([heights[1]])
    
    while unsorted:
        h = unsorted.popleft()
        changed = False
        for i in range(len(sorted)):
            if sorted[i] > h:
                sorted.insert(i, h)
                steps += len(sorted) - i - 1
                changed = True
                break
        if not changed:
            sorted.append(h)
         
    print(heights[0], steps)
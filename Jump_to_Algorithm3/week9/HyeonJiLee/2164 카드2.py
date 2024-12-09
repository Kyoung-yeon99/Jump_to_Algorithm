from collections import deque
import sys

N= int(sys.stdin.readline().rstrip())
queue=deque()
for i in range(N):
    queue.append(i+1)
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)
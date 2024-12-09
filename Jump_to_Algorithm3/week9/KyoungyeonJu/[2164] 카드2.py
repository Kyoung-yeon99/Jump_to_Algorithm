# 카드가 한 장 남을 때까지 반복
# 1. 제일 위에 있는 카들르 바닥에 버린다
# 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
from collections import deque

n = int(input())  # 1 <= n <= 500,000
d = deque([i for i in range(1, n+1)])
for _ in range(n-1):
    d.popleft()
    d.append(d.popleft())

print(d[0])
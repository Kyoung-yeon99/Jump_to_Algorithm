from collections import deque

n, k = map(int, input().split())
q = deque()
count = 1
result = []

for i in range(1, n+1): # 1부터 N까지의 숫자를 가진 덱 생성
    q.append(i)

while q:
    if count % k == 0: # k의 배수번째일 경우
        result.append(q.popleft())
    else:
        q.rotate(-1) # 덱 회전
    count += 1

print('<' + str(result)[1:-1] + '>')
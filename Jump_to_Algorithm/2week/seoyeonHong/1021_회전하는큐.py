from collections import deque

n, m = map(int, input().split())
q = deque()
count = 0

for n in range(1, n+1): # 1부터 n까지의 숫자를 가진 덱 생성
    q.append(n)

numbers = list(map(int, input().split()))

for num in numbers:
    rcount = 0

    for _ in range(n):
        if q[0] == num:
            break
        else:
            q.rotate(1) # 덱 회전
        rcount += 1
    if rcount > len(q) // 2: # q[0]과 num 사이 숫자의 개수
        count += len(q) - rcount
    else:
        count += rcount   
    
    q.popleft()

print(count)

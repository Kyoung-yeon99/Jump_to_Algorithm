from collections import deque
N, M = map(int,input().split())
ladder = dict()
snake = dict()

for _ in range(N):
    x,y = map(int,input().split())
    ladder[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

deq = deque([[1,0]])
visited = set()
visited.add(1)
while deq:
    cur_num, count = deq.popleft()
    if cur_num == 100:
        print(count)
        break

    for i in range(1,7):
        next_num = cur_num + i
        if next_num > 100:
            continue
        #뱀 타고 돌아가기
        if next_num in snake:
            next_num = snake[next_num]
        #사다리 타면
        if next_num in ladder:
            next_num = ladder[next_num] #사다리타고 이동

        if next_num not in visited:
            visited.add(next_num)
            deq.append([next_num,count+1])

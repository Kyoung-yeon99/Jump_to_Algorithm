from collections import deque

N, M = map(int, input().split())
lst = deque(range(1, N + 1))  # deque 생성
q = deque(map(int, input().split()))  # 사용자로부터 입력받은 숫자들

count = 0
while q:
    mid = len(lst) // 2  # mid 변수를 생성 lst의 중간 index로 설정
    if lst.index(q[0]) > mid:  # 만약 lst.index(q[0])가 mid보다 크다면 3번 조건 반복

        while q[0] != lst[0]:  # 반대일 경우는 2번 조건 반복
            lst.appendleft(lst.pop())
            count += 1
        lst.popleft()
        q.popleft()
    else:
        while q[0] != lst[0]:
            lst.append(lst.popleft())
            count += 1
        lst.popleft()
        q.popleft()
print(count)

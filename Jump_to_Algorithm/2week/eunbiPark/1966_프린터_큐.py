from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # 문서 개수, 현재 목표 문서 인덱스
    q = deque(list(map(int, input().split())))

    cnt = 0

    while q:
        best = max(q) # 최댓값 저장
        front = q.popleft() # 맨 앞 값 저장
        m -= 1 # 찾아야 하는 문서의 인덱스 이동

        if best == front: # 뽑은 값이 가장 큰 값이면
            cnt += 1 # 뽑혔으니 카운트 증가
            if m < 0: # 내가 뽑혔으면
                print(cnt) # 출력
                break
        else: # 뽑은 값이 가장 큰 값이 아니면
            q.append(front) # 맨 뒤로 이동
            if m < 0: # 뽑힌게 나면
                m = len(q) -1 # 맨 뒤로 갔으니 인덱스 변경
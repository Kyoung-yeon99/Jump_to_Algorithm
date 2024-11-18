from collections import deque
# 입력 처리
S = input()
T = input()

# BFS를 위해 deque 자료구조를 사용
queue = deque([T])
visited = set(T)  # 중복 상태 처리를 방지하기 위한 집합
answer = 0
while queue:
    current = queue.popleft()  # 큐에서 현재 상태 꺼내기

    # 현재 상태가 S와 같으면 변환 가능
    if current == S:
        answer = 1

    # 변환 규칙 1: 'A'로 끝나는 경우, 'A' 제거
    if current.endswith('A') and current[:-1] not in visited:
        queue.append(current[:-1])
        visited.add(current[:-1])

    # 변환 규칙 2: 'B'로 시작하는 경우, 'B' 제거 후 뒤집기
    if current.startswith('B') and current[1:][::-1] not in visited:
        queue.append(current[1:][::-1])
        visited.add(current[1:][::-1])

print(answer)  # 변환 불가능

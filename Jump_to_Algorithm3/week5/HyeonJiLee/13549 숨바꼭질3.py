import heapq
#우선순위 큐 -> 최소 시간 탐색, 최적의 해 보장 // 다익스트라(우선순위큐)
def find_brother(N, K):
    # 최대 위치 값 설정
    max_position = 100000
    # 각 위치까지의 최소 시간 무한대로 초기화 (시작노드 - 다른 모든 노드까지 거리를 무한대로 set)
    time = [float('inf')] * (max_position + 1)
    # 우선순위 큐 초기화
    queue = []
    heapq.heappush(queue, (0, N))  # (시간, 위치)
    time[N] = 0

    while queue:
        current_time, current_position = heapq.heappop(queue)

        # 동생의 위치에 도달했다면 최단 시간 반환
        if current_position == K:
            return current_time

        # 이미 기록된 최단 시간이 더 짧다면 넘어감
        if current_time > time[current_position]:
            continue

        # 세 가지 이동 방식에 따라 다음 위치와 시간 계산
        for next_position, additional_time in [
            (current_position * 2, 0),    # 순간이동: 가중치 0
            (current_position + 1, 1),    # 걷기: 가중치 1
            (current_position - 1, 1)     # 걷기: 가중치 1
        ]:
            # 다음 위치가 유효한 범위 내에 있어야 함
            if 0 <= next_position <= max_position:
                new_time = current_time + additional_time
                # 새로운 시간이 기록된 시간보다 작으면 갱신
                if new_time < time[next_position]:
                    time[next_position] = new_time
                    heapq.heappush(queue, (new_time, next_position))

N, K = map(int, input().split())
print(find_brother(N, K))

from collections import deque


def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    answer = 100

    for w in wires:  # 전선 정보를 통해 트리 생성
        v1, v2 = w
        tree[v1].append(v2)
        tree[v2].append(v1)

    for w in wires:  #
        v1, v2 = w
        visited = [0]*(n+1)
        connected_towers, qu = [], deque([v1])  # 연결된 송전탑 리스트, queue

        while qu:
            v = qu.popleft()
            for i in tree[v]:
                if i != v1 and i != v2:
                    if visited[i] == 0:
                        connected_towers.append(i)
                        visited[i] = 1
                        qu.append(i)

        ans = len(connected_towers) + 1  # 연결된 송전탑과 자신의 송전탑
        answer = min(answer, abs(2*ans-n))  # 두 전력망의 송전탑 개수 차이 최소값

    return answer
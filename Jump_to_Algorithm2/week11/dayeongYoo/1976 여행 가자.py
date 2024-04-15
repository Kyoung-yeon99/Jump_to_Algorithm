# 도시가 N개 있고 임의의 두 도시 사이에 길이 있다.
# 중간에 다른 도시를 경유해서 여행을 할 수 있다.
# 같은 도시를 여러 번 방문하는 것도 가능하다.

# https://velog.io/@rhkswls98/%EB%B0%B1%EC%A4%80-1976-C-%EC%97%AC%ED%96%89-%EA%B0%80%EC%9E%90

import sys


def solution(start):
    stack = [start]  # 첫 도시 출발점

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1  # 해당 도시 여행 가능
            for next in range(N):  # 해당 도시와 연결된 도시들 탐색
                if linked[node][next]:
                    stack.append(next)  # 연결된 다음 도시 여행


N = int(sys.stdin.readline())  # 도시의 수
M = int(sys.stdin.readline())  # 여행 계획 도시 수
linked = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 도시들 간 연결 정보
want = list(map(int, sys.stdin.readline().split()))  # 여행 계획

visited = [0] * N  # 도시 방문 가능 여부

solution(want[0] - 1)  # 여행 계획의 첫 도시를 출발점으로 탐색

for w in want:
    if not visited[w - 1]:  # 여행 계획에 있는 도시를 방문 가능한 경로가 없다면
        print('NO')  # NO 출력
        break
else:  # 원하는 모든 도시 방문 가능하다면
    print('YES')  # YES 출력

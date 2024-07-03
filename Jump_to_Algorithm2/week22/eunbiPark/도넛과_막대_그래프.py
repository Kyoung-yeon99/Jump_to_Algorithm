def solution(edges):
    ans = [0, 0, 0, 0]
    n = 0  # 노드 수
    for ed in edges:
        n = max(n, max(ed))

    # 0. 인접 그래프 생성
    graph = [[] for _ in range(n + 1)]  # 나가는 것
    in_graph = [[] for _ in range(n + 1)]  # 들어오는 것 - 생성한 정점 찾기에 활용

    for ed in edges:
        graph[ed[0]].append(ed[1])
        in_graph[ed[1]].append(ed[0])

    # 1. 생성한 정점 찾기
    # 생성한 정점: 나가는 것 2개 이상, 들어오는 것 0개 인 노드

    # 2. 그래프 개수 세기
    # 특정 노드를 대표하는 노드의 특성이 있음
    # 막대: 나가는 간선: 0 이상, 들어오는 간선: 1 이상
    # 8자: 나가는 간선: 2, 들어오는 간선: 2 이상
    # 도넛: 생성 정점에서 나가는 간선 - 막대 개수 - 8자 개수
    # !주의!: 생성한 정점에서 나오는 간선도 생각해야 함 (없는 노드라고 생각하지 않기)
    for i in range(1, n + 1):
        # 1. 생성한 정점
        if len(graph[i]) > 1 and len(in_graph[i]) == 0:
            ans[0] = i
        # 2. 막대 그래프
        if len(graph[i]) == 0 and len(in_graph[i]) >= 1:
            ans[2] += 1
        # 3. 8자 그래프
        if len(graph[i]) == 2 and len(in_graph[i]) >= 2:
            ans[3] += 1
    # 4. 도넛 그래프
    ans[1] = len(graph[ans[0]]) - ans[2] - ans[3]

    return ans

'''
# 그래프 탐색 시도 <- 그래프의 크기가 커서 안된다 
# 2-1. 생성한 정점과 연결된 노드 지우기 
    graph[make] = []
    
    # 도넛 
    print(f'graph: {graph}')
    q = deque()
    visited = [0 for _ in range(n + 1)]
    line, donut, eight = 0, 0, 0
    check = []

    for i in range(1, n + 1):
        if graph[i] and not visited[i]:
            q.append(i)
        flag = True  # 라인 판단 

        while q:
            x = q.popleft()
            visited[x] = 1
            for nx in graph[x]:
                if not visited[nx]:
                    q.append(nx)

                if visited[nx]:
                    flag = False
                    donut += 1
                    if check == []:
                        check = [x, nx]
                    else:
                        if x in check or nx in check:
                            eight += 1
                            donut -= 2
                        check = []


        if graph[i] and flag:
            line += 1
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 오답..

# 풀이1
from collections import deque

def solution(edges):
    n = 0
    for edge in edges:
        n = max(n, max(edge))

    answer = [0, 0, 0, 0] # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    index = {'new': 0, 'donut': 1, 'bar': 2, 'eight': 3}
    after = {i: [] for i in range(1, n+1)} # 다음 노드 리스트
    before = {i: [] for i in range(1, n+1)} # 이전 노드 리스트
    visited = {i: False for i in range(1, n+1)} # 방문 여부
    
    for edge in edges:
        a, b = edge
        after[a].append(b)
        before[b].append(a)
            
    for i in range(1, n+1):
        if before[i] == [] and len(after[i]) >= 2: # 새로 생성한 정점일 경우
            visited[i] = True
            answer[index['new']] = i
            for node in after[i]:
                before[node].remove(i)
            print(f'{i} is new node')
            
    for i in range(1, n+1):
        if not visited[i]: # 아직 확인되지 않은 정점일 경우
            if before[i] == []: # 막대 모양 그래프의 시작 정점일 경우
                cur = i
                print(f'bar graph: {i}', end=' ')
                while True:
                    visited[cur] = True
                    if after[cur] == []:
                         break
                    else:
                        cur = after[cur][0]
                        print(f'{cur}', end=' ')
                        
                answer[index['bar']] += 1
    print()
    for i in range(1, n+1):
        if not visited[i]: # 아직 확인되지 않은 정점일 경우
            node, edge = 0, 0
            q = deque([i])
            visited[i] = True
            print(f'group:', end=' ')
            while q:
                cur = q.popleft()
                node += 1
                print(cur, end=' ')
                for next in after[cur]:
                    edge += 1
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
            if node == edge:
                answer[index['donut']] += 1
            else:
                answer[index['eight']] += 1
            print(f'node: {node}, edge: {edge}')
            
    return answer


# 풀이2
from collections import deque

def solution(edges):
    n = 0
    for edge in edges:
        n = max(n, max(edge))

    answer = [0, 0, 0, 0] # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    index = {'new': 0, 'donut': 1, 'bar': 2, 'eight': 3}
    after = {i: [] for i in range(1, n+1)} # 다음 노드 리스트
    before = {i: [] for i in range(1, n+1)} # 이전 노드 리스트
    visited = {i: False for i in range(1, n+1)} # 방문 여부
    
    for edge in edges:
        a, b = edge
        after[a].append(b)
        before[b].append(a)

            
    for i in range(1, n+1):
        if before[i] == [] and len(after[i]) >= 2: # 새로 생성한 정점일 경우
            visited[i] = True
            answer[index['new']] = i
            for node in after[i]:
                before[node].remove(i)
            print(f'{i} is new node')
            
    print()
    # 도넛 그래프와 8자 모양 그래프 확인
    for i in range(1, n+1):
        if not visited[i]: # 아직 확인되지 않은 정점일 경우
            circular = False
            node, edge = 0, 0
            q = deque([i])
            visited[i] = True
            print(f'group:', end=' ')
            while q:
                cur = q.popleft()
                node += 1
                print(cur, end=' ')
                for next in after[cur]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
                        
                for next in before[cur]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
                    else:
                        circular = True
                    edge += 1
                
            if node == edge:
                answer[index['donut']] += 1
                print('-> donut', end='')
            elif circular:
                answer[index['eight']] += 1
                print('-> eight', end='')
            else:
                answer[index['bar']] += 1
                print('-> bar', end='')
            print(f',node: {node}, edge: {edge}')
            
    return answer
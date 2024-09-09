# https://school.programmers.co.kr/learn/courses/30/lessons/86971?language=python3

# 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때 두 전력망이 가지고 있는 송전탑 개수의 차이
from collections import defaultdict, deque

def solution(n, wires):
    min_diff = int(1e9)
    adj = defaultdict(list) # 인접 노드 리스트
    
    def bfs(sv): # 너비 우선 탐색
        count = 0
        q = deque([sv])
        visited = [False for _ in range(len(adj) + 1)]
        visited[sv] = True
        
        while q:
            v = q.popleft()
            count += 1
            for nv in adj[v]:
                if not visited[nv]:
                    q.append(nv)
                    visited[nv] = True
        
        return count # 전력망을 이루는 송전탑의 개수 반환
        
    
    def calculate_diff(v1, v2): # 두 전력망을 이루는 송전탑 개수의 차이 계산
        t1 = bfs(v1)
        t2 = bfs(v2)
        
        return abs(t1 - t2)
    
    for wire in wires:
        v1, v2 = wire 
        adj[v1].append(v2)
        adj[v2].append(v1)
        
    for wire in wires: # v1, v2를 잇는 전선을 끊을 경우
        v1, v2 = wire
        adj[v1].remove(v2)
        adj[v2].remove(v1)
        
        diff = calculate_diff(v1, v2)
        min_diff = min(min_diff, diff) # 최댓값 갱신
        
        adj[v1].append(v2)
        adj[v2].append(v1)
    
        
    return min_diff
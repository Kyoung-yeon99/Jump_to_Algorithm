from collections import deque

t = int(input()) # 테스트 케이스 개수

def available(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) <= 1000

for _ in range(t):
    arrived = False # 도착 여부

    n = int(input()) # 편의점의 개수

    home = list(map(int, input().split())) # 집 위치

    stores = [] # 가게 위치
    for _ in range(n):
        stores.append(list(map(int, input().split())))

    festival = list(map(int, input().split())) # 페스티벌 위치

    visited = [False] * n # 가게 방문 여부

    graph = [[] for _ in range(n+1)] # i번째 가게에서 갈 수 있는 가게의 목록 (n번째는 집)

    for i in range(n-1):
        for j in range(i+1, n):
            if available(stores[i], stores[j]):
                graph[i].append(j)
                graph[j].append(i)
        
    for i in range(n):    
        if available(home, stores[i]):
            graph[n].append(i)


    if available(home, festival): # 집에서 페스티벌로 바로 갈 수 있을 경우
        print("happy")
    else: # 바로 갈 수 없는 경우
        q = deque()
        for storeNum in graph[n]: # 집에서 바로 갈 수 있는 가게 목록 추가
            q.append(storeNum)
        while q:
            num = q.popleft()
            print(num)
            if available(stores[num], festival): # 가게를 거쳐 페스티벌에 갈 수 있는 경우
                print("happy")
                arrived = True
                break
            else: # 가게에서 페스티벌에 갈 수 없는 경우
                for i in graph[num]: # 현재 가게에서 갈 수 있는 다른 가게 추가
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
        if not arrived:
            print("sad")

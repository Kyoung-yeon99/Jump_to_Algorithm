# 물에 잠기지 않는 영역의 최대 개수
from collections import deque

n = int(input()) # 배열의 크기
a = [] # 영역의 높이 배열
numSet = set()
for _ in range(n):
    row = list(map(int, input().split()))
    numSet.update(row)
    a.append(row)
numSet = sorted(numSet) # 영역의 높이 집합
maxNum = 1 # 물에 잠기는 영역이 없을 경우

for h in numSet[:-1]: # h이하는 잠김, 가장 낮은 지역 높이부터 2번째로 높은 지역 높이까지
    q = deque() # 방문할 영역
    num = 0 # 안전영역의 개수
    visited = [[[] for _ in range(n)] for _ in range(n)] # 방문 여부 체크
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and a[i][j] > h: # 물에 잠기지 않고 방문하지 않은 영역일 경우
                num += 1 # 영역 개수 +1
                q.append((i, j))
                visited[i][j] = True
                count = 0
                while q:
                    count += 1
                    r, c = q.popleft()
                    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                        if 0 <= nr < n and 0 <= nc < n: # nr, nc가 0이상 n미만일 경우
                            if not visited[nr][nc]: # 방문 여부 체크
                                visited[nr][nc] = True
                                if a[nr][nc] > h: # 물에 잠기지 않은 인접한 영역일 경우 방문 리스트에 추가
                                    q.append((nr, nc))
                                    
    if num > maxNum:
        maxNum = num

print(maxNum)




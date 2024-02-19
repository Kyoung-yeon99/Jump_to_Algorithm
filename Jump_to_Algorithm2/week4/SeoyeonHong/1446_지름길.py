# 운전해야 하는 거리의 최솟값
import sys
input = sys.stdin.readline
N, D = map(int, input().split()) # 지름길의 개수 N, 고속도로의 길이 D
min_distance = {0: 0}
shortcut = [] # 지름길 정보
ans = D
for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        shortcut.append([s, e, d])
        min_distance[s] = s
        min_distance[e] = e

min_distance[D] = D
shortcut.append([D, D, 0])
shortcut.sort(key=lambda way: (way[1], way[0]))

def searchWay(ways, sum):
    global ans
    cur = ways[-1]
    if cur == D:
        ans = min(ans, sum)
    else:
        for way in shortcut:
            s, e, d = way
            if s >= cur: # 길의 시작 위치가 현재 위치보다 앞일 경우
                if min_distance[e] > min_distance[cur] + s - cur + d:
                    min_distance[e] = min_distance[cur] + s - cur + d
                    ways.append(e)
                    searchWay(ways, min_distance[e])
                    ways.pop()
            
searchWay([0], 0)
print(ans)



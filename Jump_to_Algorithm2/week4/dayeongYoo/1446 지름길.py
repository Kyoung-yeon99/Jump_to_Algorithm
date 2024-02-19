# 지름길: 일반통행, 역주행 불가
# 거리의 최솟값?

# 지름길 n, 고속도로 길이 d
n, d = map(int, input().split())
# 지름길
fastway = [list(map(int, input().split())) for _ in range(n)]

# 거리 갱신할 리스트
way = [x for x in range(d + 1)]  # index-error 방지용

# 0~d까지 거리 체크
for i in range(d + 1):
    # 지름길 vs 고속도로
    way[i] = min(way[i], way[i - 1] + 1)
    # 지름길을 반복해 최단거리 찾기
    for start, end, fastest in fastway:
        # 고속도로보다 지름길이 빠른 경우
        if i == start and end <= d and way[i] + fastest < way[end]:
            # 최단거리 갱신
            way[end] = way[i] + fastest
# 목적지에 도착했을 때 걸린 거리 출력
print(way[d])

'''
0 50 10보다 0 50 20을 가는게 이득
if fastway[0]==fastway[1]: # 시작, 끝이 같을 경우
    ans += max (fastway[2])

2 100
10 60 40
50 90 20

--> ??

-------------완전 잘못 생각하고 있었음.;;

예시1) 0~50까지 지름길 10을 쓰고, 50~100까지 10.
그리고 그냥 100~150은 고속도로 타는게(50) 빠름.
=> 70
지름길이 지름길이 아닐 수 있음 주의.

예시2) 0~50까지 고속도로(50), 50~90까지 지름길(20), 그리고 90~100 고속도로(10)
=> 80


'''

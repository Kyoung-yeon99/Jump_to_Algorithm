import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()  # 오름차순 정렬
min_d = 1  # 최소 거리 차이
max_d = houses[n-1] - houses[0]  # 최대 거리 차이

while min_d <= max_d:
    mid_d = (min_d+max_d)//2  # 중간 거리 차이
    cnt = 1  # 첫번째 집은 항상 공유기 설치
    last = houses[0]  # 마지막으로 공유기 설치한 집의 좌표
    for i in range(1, n):
        if houses[i] - last >= mid_d:  # 거리 차이가 중간 거리 차이 이상이면
            cnt += 1
            last = houses[i]  # 마지막 공유기 설치 집 갱신

    if cnt >= c:  # 중간 거리가 작기 때문에 최소 거리 증가
        min_d = mid_d + 1
    else:  # 중간 거리가 크기 때문에 최대 거리 감소
        max_d = mid_d - 1

print(min_d-1)

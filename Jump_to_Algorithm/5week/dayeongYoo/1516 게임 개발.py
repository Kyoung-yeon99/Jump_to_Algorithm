n = int(input())  # 건물 개수
buildings = []
for _ in range(n):
    buildings.append(list(map(int, input().split()[:-1])))  # -1를 제외하고 건물 짓는 시간, 먼저 지어져야하는 건물 번호 저장
# 각 빌딩 짓는데 걸리는 최소 시간
times = [0] * n


# 건물 짓는 최소 시간 구하기
def get_build_minimum(i, build_time, pre_buildings):
    if pre_buildings:  # 선행되어야 하는 건물이 있다면
        # 짓는 시간 비교
        max_time, pre_time = 0, 0
        for b in pre_buildings:
            # cashing 해논 값이 아니라면 최초 한번은 계산해준다.
            if times[b - 1] == 0:  # 리스트의 인덱스는 0 base 이므로 -1해준다
                pre_time = get_build_minimum(b - 1, buildings[b - 1][0], buildings[b - 1][1:])
            else:  # 캐싱해논 값이 있다면
                pre_time = times[b - 1]
            if max_time < pre_time:
                max_time = pre_time
        times[i] = max_time + build_time  # 건설 시간 갱신
        return max_time + build_time  # 반환

    else:  # 선행되어야 하는 건물이 없다면
        times[i] = build_time
        return build_time


# 실행
for i in range(n):
    if times[i] == 0:  # 구하지 않은 값이라면
        # 건물번호, 걸리는 시간, 먼저 지어져야하는 건물번호 리스트를 매개변수로 함수 실행
        get_build_minimum(i, buildings[i][0], buildings[i][1:])
# 출력
for time in times:
    print(time)

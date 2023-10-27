# https://www.acmicpc.net/problem/1911

n, length = map(int, input().split())  # 물웅덩이 개수, 널빤지 길이
water_holes = [list(map(int, input().split())) for _ in range(n)]  # 모든 물웅덩이 저장

water_holes.sort()  # 물 웅덩이를 더할때 순서대로 널빤지를 대어서 최소 널빤지 개수 구함
ans = 0  # 널빤지 개수

for i in range(n):
    st, end = water_holes[i]  # 시작, 끝위치
    width = (end - st)  # 웅덩이 크기

    if width % length != 0:  # 물웅덩이를 널빤지로 다 덮지 못하면
        bridge_num = width // length + 1  # 1개 추가함.
    else:
        bridge_num = width // length  # 물웅덩이를 널빤지로 다 덮을 경우

    ans += bridge_num  # 총 널빤지 개수에 추가
    # 새로운 끝 = 시작위치 + (널빤지 길이 x 필요한 널빤지 개수)
    new_end = st + length * bridge_num  # 그 다음 물웅덩이를 끌어다 최소로 덮기 위해

    if (i + 1) < n:  # 다음 널빤지 탐색
        next_st = water_holes[i + 1][0]
        if new_end > next_st:  # 널빤지가 다음 웅덩이까지 덮을 때
            water_holes[i + 1][0] = new_end
print(ans)

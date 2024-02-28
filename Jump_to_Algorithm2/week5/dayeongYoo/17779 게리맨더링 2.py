n = int(input())
# 인구: 2차원 배열
population = [list(map(int, input().split())) for _ in range(n)]


def solve():
    min_ans = 20 * 20 * 100  # 인구 차이를 최댓값으로 리셋

    # 도시 경계의 좌표(x,y)
    for x in range(n):
        for y in range(n):
            # 거리: d1
            for d1 in range(1, n + 1):
                # 거리: d2
                for d2 in range(1, n + 1):
                    # 나머지 세 모서리가 범위 내에 있어야 한다.
                    if (0 <= x + d1 < n and 0 <= y - d1 < n) and (0 <= x + d2 < n and 0 <= y + d2 < n) and (
                            0 <= x + d1 + d2 < n and 0 <= y - d1 + d2 < n):
                        # 도시 나누기(어느 구역에도 속하지 않는 선거구 5로 초기화)
                        section = [[5 for _ in range(n)] for _ in range(n)]

                        # 1번 구역 설정
                        for i in range(d1 + 1):
                            r1, c1 = x + i, y - i
                            for tr in range(r1):
                                section[tr][c1] = 1

                        r2, c2 = x + d1, y - d1
                        for tc in range(c2):
                            for tr in range(r2):
                                section[tr][tc] = 1

                        # 2번 구역 설정
                        for i in range(d2 + 1):
                            r1, c1 = x + i, y + i  # 시작점(d2만큼 이동)
                            for tc in range(c1 + 1, n):  # c1부터 끝까지
                                section[r1][tc] = 2  # 2번 구역으로 설정

                        r2, c2 = x, y  # 시작점
                        for tr in range(r2):  # 도시 위쪽으로 반복.
                            for tc in range(c2 + 1, n):  # c2부터 끝까지
                                section[tr][tc] = 2  # 2번 구역으로 설정

                        # 3번 구역 설정
                        for i in range(d2 + 1):
                            r1, c1 = x + d1 + i, y - d1 + i
                            for tc in range(c1):
                                section[r1][tc] = 3

                        r2, c2 = x + d1 + d2, y - d1 + d2
                        for tr in range(r2 + 1, n):
                            for tc in range(c2):
                                section[tr][tc] = 3

                        # 4번 구역 설정
                        for i in range(d1 + 1):
                            r1, c1 = x + d2 + i, y + d2 - i
                            for tr in range(r1 + 1, n):
                                section[tr][c1] = 4

                        r2, c2 = x + d2, y + d2
                        for tc in range(c2 + 1, n):
                            for tr in range(r2 + 1, n):
                                section[tr][tc] = 4

                        cal = [0 for _ in range(6)]  # 5번 구역까지

                        # 인구 계산
                        for r in range(n):
                            for c in range(n):
                                sec = section[r][c]
                                cal[sec] += population[r][c]
                        ans = max(cal[1:]) - min(cal[1:])  # 1~5번 구역의 최댓값-최솟값

                        if min_ans > ans:  # 최솟값 갱신
                            min_ans = ans

    print(min_ans)


solve()

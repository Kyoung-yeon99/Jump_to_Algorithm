n = int(input())  # n일 동안 상담
T = []  # 상담 걸리는 기간
P = []  # 금액
for _ in range(n):
    t, p = map(int, input().split())  # 공백을 기준으로 입력받음
    # 각각을 상담기간, 금액 리스트에 추가
    T.append(t)
    P.append(p)

cache = [-1] * n  # cache 테이블 생성


def dp(i):
    if i >= n:  # 가능한 상담일수와 같거나 클때는 0
        return 0
    # 한번도 계산해주지 않았다면
    if cache[i] == -1:
        # 일 안하고 그냥 넘어갈 경우
        cache[i] = dp(i + 1)

        # 일을 시작할 경우
        if i + T[i] <= n:  # 상담일 수 + 상담 걸리는 기간이 가능한 상담일 수보다 작거나 같을때
            cache[i] = max(cache[i], P[i] + dp(i + T[i]))

    return cache[i]


print(dp(0))

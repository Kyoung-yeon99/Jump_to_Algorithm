n = int(input())

cache = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):  # index error 방지
    for j in range(i + 1):
        # 층의 첫번째 숫자
        if j == 0:
            cache[i][j] += cache[i - 1][0]
        # 층의 마지막 숫자
        elif i == j:
            cache[i][j] += cache[i - 1][-1]
        # 대각선 2개가 만나는 지점
        else:
            cache[i][j] += max(cache[i - 1][j - 1], cache[i - 1][j])

# 정답
ans = -1

for c in cache:
    c.sort(reverse=True)  # 내림차순 정렬
    ans = max(c[0], ans)
print(ans)
ㅈ
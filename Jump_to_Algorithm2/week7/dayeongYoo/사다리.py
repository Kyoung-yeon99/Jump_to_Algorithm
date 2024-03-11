# 두개의 사다리가 있고 길이가 x, y이다.
# 그리고 두 사다리는 땅에서부터 높이가 c인지점에서 정확하게 교차한다.
# 이때 두 빌딩사이의 거리는?

# https://velog.io/@qlql323/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-2022-%EC%82%AC%EB%8B%A4%EB%A6%AC

x, y, c = map(float, input().split())
high = min(x, y)
low = 1
ans = 0
while low + 0.001 <= high:
    w = (low + high) / 2
    # w를 이용해서 c계산
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    guess_c = (h1 * h2) / (h1 + h2)
    if guess_c >= c:
        ans = w
        low = w
    else:
        high = w
print(ans)

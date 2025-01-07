N = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(N):
    cnt = 0  # 보이는 빌딩 수

    # 오른쪽 기울기 비교
    max_right = -1000000001  # 기울기 초기화 (가장 작은 값으로 설정)
    for j in range(i + 1, N):
        x1, y1 = i, arr[i]
        x2, y2 = j, arr[j]

        a = (y2 - y1) / (x2 - x1)  # 기울기 계산

        if a > max_right:  # 이전 기울기보다 더 큰 기울기일 경우만 보인다
            max_right = a
            cnt += 1

    # 왼쪽 기울기 비교
    max_left = 1000000001   # 기울기 초기화 (가장 큰 값으로 설정)
    for j in range(i - 1, -1, -1):
        x1, y1 = i, arr[i]
        x2, y2 = j, arr[j]

        a = (y2 - y1) / (x2 - x1)  # 기울기 계산

        if a < max_left:  # 이전 기울기보다 더 작은 기울기일 경우만 보인다
            max_left = a
            cnt += 1

    answer = max(answer, cnt)

print(answer)

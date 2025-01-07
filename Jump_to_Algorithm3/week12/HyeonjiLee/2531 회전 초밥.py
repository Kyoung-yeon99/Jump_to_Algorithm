from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

max_type = 0
cnt = defaultdict(int)

# 처음 k개의 접시에서 초밥 종류 세기
for i in range(k):
    cnt[belt[i]] += 1

# 쿠폰 번호도 고려해서 한번 먹을 수 있다고 설정
sushi_type = len(cnt) + (1 if c not in cnt else 0)
max_type = max(max_type, sushi_type)

# 슬라이딩 윈도우로 벨트를 한 바퀴 돌며 최대 초밥 가짓수 구하기
for i in range(1, N):
    # 윈도우를 오른쪽으로 한 칸 이동
    cnt[belt[(i + k - 1) % N]] += 1  # 새로 들어온 초밥
    cnt[belt[i - 1]] -= 1  # 벗어난 초밥

    # 벗어난 초밥이 0이 되면 초밥 제거
    if cnt[belt[i - 1]] == 0:
        del cnt[belt[i - 1]]

    # 쿠폰 번호 초밥을 추가로 고려
    sushi_type = len(cnt) + (1 if c not in cnt else 0)
    max_type = max(max_type, sushi_type)

# 결과 출력
print(max_type)

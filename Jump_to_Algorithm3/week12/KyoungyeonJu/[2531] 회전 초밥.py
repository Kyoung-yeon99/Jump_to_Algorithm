# 최대한 다양항 종류의 초밥 먹기
# 초밥 벨트 위 접시 수 N, 초밥 가짓수 d, 연속해서 먹는 접시 수 k, 쿠폰 번호 c
# 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
answer = 1

for i in range(N):
    if i > N-k:
        k_sushi = set(sushi[i:N]+sushi[:k-(N-i)])
    else:
        k_sushi = set(sushi[i:i+k])

    if c not in k_sushi:
        answer = max(answer, len(k_sushi)+1)
    else:
        answer = max(answer, len(k_sushi))

print(answer)

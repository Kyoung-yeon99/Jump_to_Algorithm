# 손님이 먹을 수 있는 초밥 가짓수의 최댓값
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = []
max_count = 1

for _ in range(N):
    sushi.append(int(input()))

selected = sushi[:k] + [c] # 고른 초밥 + 쿠폰
s = 0
for _ in range(N):
    print(selected)
    max_count = max(max_count, len(set(selected)))
    selected.remove(sushi[s % N])
    selected.append(sushi[(s+k) % N])
    s += 1

print(max_count)
# n개의 집 r,g,b로 색칠

n = int(input())
# 갱신할 cache 리스트
cache = []

for i in range(n):
    cache.append(list(map(int, input().split())))
# rgb 색칠
for i in range(1, len(cache)):
    # r
    cache[i][0] = min(cache[i - 1][1], cache[i - 1][2]) + cache[i][0]
    # g
    cache[i][1] = min(cache[i - 1][0], cache[i - 1][2]) + cache[i][1]
    # b
    cache[i][2] = min(cache[i - 1][0], cache[i - 1][1]) + cache[i][2]
# 최솟값 출력
print(min(cache[n - 1][0], cache[n - 1][1], cache[n - 1][2]))

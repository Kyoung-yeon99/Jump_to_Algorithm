n = int(input()) # 배열의 크기
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# 판다가 이동할 수 있는 칸의 최댓값
# 판다는 더 큰 수로만 이동


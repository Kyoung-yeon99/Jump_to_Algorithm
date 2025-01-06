# 가장 많은 고층 빌딩이 보이는 빌딩에서 보이는 빌딩의 수
N = int(input()) # 빌딩의 수
heights = list(map(int, input().split())) # 빌딩들의 높이
max_count = 0
for i in range(N):
    
    count = 0
    last_slope = 1000000000
    h = heights[i]
    for j in range(1, i+1): # 왼쪽으로 갈수록 직선의 기울기가 작아져야 함
        slope = (h - heights[i-j]) / j
        if slope < last_slope:
            last_slope = slope
            count += 1

    last_slope = -1000000000
    for j in range(1, N-i): # 오른쪽으로 갈수록 직선의 기울기가 커져야 함
        slope = (heights[i+j] - h) / j
        if slope > last_slope:
            last_slope = slope
            count += 1
    
    max_count = max(max_count, count)

print(max_count)

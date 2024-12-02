H, W = map(int, input().split())
blocks = list(map(int, input().split()))   
total_water = 0

for i in range(1, len(blocks)-1): # 양쪽 마지막 칸을 제외하고 각 열에 대해
    left = max(blocks[:i])
    right = max(blocks[i:])

    water = min(left, right) - blocks[i] # 빗물의 양 = 왼쪽과 오른쪽의 최댓값 중 더 작은 것 - 블록의 높이
    if water > 0:
        total_water += water

print(total_water)
    

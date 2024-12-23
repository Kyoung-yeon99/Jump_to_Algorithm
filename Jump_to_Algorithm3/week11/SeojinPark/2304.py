n = int(input())
col = []
[col.append(list(map(int, input().split()))) for _ in range(n)]

col.sort()

# 가장 높은 기둥
i=0
max_height = 0
for c in col:
    if c[1] > max_height:
        max_height=c[1]
        max_height_index = i
    i+=1

area = 0
height = col[0][1]

# index 0 ~ max_height_index 까지 포함되는 넓이 합
# 다음 기중이 현재보다 높으면 갱신
for i in range(0, max_height_index):
    if height < col[i+1][1]:
        area += height * (col[i+1][0] - col[i][0])
        height=col[i+1][1]
    else:
        area += height * (col[i+1][0] - col[i][0])

# 가장 뒤에 있는 기둥 기준
height = col[-1][1]

# index max_height_index ~ n 까지 포함되는 넓이 합
for i in range(n-1, max_height_index, -1):
    if height < col[i-1][1]:
        area += height * (col[i][0] - col[i-1][0])
        height=col[i-1][1]
    else:
        area += height * (col[i][0] - col[i-1][0])

# 가장 높은 기둥
area += max_height
print(area)

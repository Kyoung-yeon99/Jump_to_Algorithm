def bingo(matrix):
    cnt = 0
    for i in range(5):  # 가로 확인
        if sum(matrix[i]) == 0:
            cnt += 1
    new_m = list(zip(*matrix))
    for i in range(5):  # 세로 확인
        if sum(new_m[i]) == 0:
            cnt += 1
    is_d1 = True
    for x in range(5):
        if matrix[x][x] != 0: # 왼상-> 오하
            is_d1 = False
    if is_d1:
        cnt += 1

    is_d2 = True
    for x in range(5):
        if matrix[x][4-x] != 0:
            is_d2 - False
    if is_d2:
        cnt += 1

    return cnt


chulsoo = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(list(map(int, input().split())))

for num in nums:
    for i in range(5):
        for j in range(5):
            if chulsoo[i][j] == num:
                chulsoo[i][j] = 0
                if bingo(chulsoo) >= 3:
                    print(nums.index(num)+1)
                    exit()


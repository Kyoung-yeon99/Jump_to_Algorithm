bingo = []
nums = []
count = 0
for _ in range(5):
    bingo.append(list(map(int, input().split())))
for _ in range(5):
    nums.extend(list(map(int, input().split())))

row = [0 for _ in range(5)]
column = [0 for _ in range(5)]
descending_diagonal = 0
ascending_diagonal = 0

def check_bingo():
    line = row.count(5) + column.count(5)
    if descending_diagonal == 5:
        line += 1
    if ascending_diagonal == 5:
        line += 1
    if line > 2:
        return True
    else:
        return False

for n in nums:
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == n:
                count += 1
                row[r] += 1
                column[c] += 1
                if r == c:
                    descending_diagonal += 1
                if (r+c) == 4:
                    ascending_diagonal += 1
                if check_bingo() is True:
                    print(count)
                    exit()

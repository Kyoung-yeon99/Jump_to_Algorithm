x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in range(7):
    if stick[i] <= x:
        x -= stick[i]
        cnt += 1

print(cnt)

N = int(input())
cnt = 1
total = 1
while True:
    if N <= total:
        break
    total += 6 * cnt
    cnt+=1
print(cnt)
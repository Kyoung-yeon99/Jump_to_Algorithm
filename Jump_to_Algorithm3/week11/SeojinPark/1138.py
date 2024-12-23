n = int(input())
higher = list(map(int, input().split()))
res = [int(1e9)]*n

for i in range(n):
    cnt = 0
    j=0
    k = higher[i]
    while j<n:
        if cnt == k:
            if res[j] == int(1e9):
                res[j] = i+1
                break
        if res[j] > (i+1):
            cnt += 1
        j+=1
print(*res)

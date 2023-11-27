n, k = map(int, input().split())
a = list(map(int, input().split()))
multi = []
cnt = 0

for i in range(k):
    if a[i] in multi:
        continue

    if len(multi) < n:
        multi.append(a[i])
        continue

    idxs = []
    for m in multi:
        if m in a[i:]:
            idxs.append(a[i:].index(m))
        else:
            idxs.append(101)
    rm = idxs.index(max(idxs))
    multi.remove(multi[rm])
    multi.append(a[i])
    cnt += 1

print(cnt)
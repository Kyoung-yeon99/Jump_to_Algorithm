h, w = map(int, input().split())
block = list(map(int, input().split()))
res=0
for i in range(1, w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    m = min(left, right)
    if m>block[i]:
        res+=(m-block[i])
print(res)
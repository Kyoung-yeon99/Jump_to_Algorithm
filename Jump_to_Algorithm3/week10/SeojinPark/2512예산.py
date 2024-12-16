n=int(input())
cost = list(map(int,input().split()))
total_limit = int(input())

#이분탐색
low, high = 0, max(cost) # 각 지역의 예산의 최대 최소
ans=0
while low<=high:
    total=0
    mid = (low+high)//2 # 중간값
    for i in cost:
        total += min(i, mid)
    if total_limit<total:
        high = mid-1
    else:
        low = mid+1
        ans=mid
print(ans)


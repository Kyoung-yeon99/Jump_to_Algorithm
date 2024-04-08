# https://velog.io/@qlwb7187/13305%EC%A3%BC%EC%9C%A0%EC%86%8C-%EA%B7%B8%EB%A6%AC%EB%94%94python

N = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))

minprice = price[0]
ans = 0

for i in range(N - 1):
    if minprice > price[i]:  # 현재까지의 최소 가격보다 새로운 가격이 더 작을 때 업데이트
        minprice = price[i]

    ans += (minprice * city[i])

print(ans)

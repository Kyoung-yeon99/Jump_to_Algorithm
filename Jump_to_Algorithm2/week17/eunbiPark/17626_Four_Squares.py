n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수는 1로 저장

min_ = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n] : # n이 제곱수일 경우
        min_=1
        break
    elif arr[n-i**2] : # 나머지가 제곱수일 경우
        min_=2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_=3
print(min_)

'''
n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    min_ = 4
    j = 1
    while (j**2) <= i:
        min_ = min(min_, dp[i-j**2])
        j += 1
    dp.append(min_ + 1)
print(dp[n])
'''
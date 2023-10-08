# GCD 합
# 최대공약수 반환하는 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


t = int(input())  # 테스트 케이스  개수
arr = []
row_sum = 0
for i in range(t):
    row = list(map(int, input().split()))
    row_num = row[0]
    row_arr = row[1:]
    arr.append(row_arr)  # 2차원 배열 각 행마다 테스트 케이스

for x in range(len(arr)):  # 각 행마다
    a_len = len(arr[x])
    for i in range(a_len-1):
        for j in range(i+1, a_len):
            result = gcd(arr[x][i], arr[x][j])
            row_sum = sum + result

    print(row_sum)
    row_sum = 0
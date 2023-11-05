n = int(input())  # 1 <= n <= 1000
d = [[0]*10 for i in range(1000)]  # 수는 0으로 시작 가능, 0 ~ 9
result = 0

for i in range(10):  # 첫번째 행 1로 초기화
    d[0][i] = 1

for i in range(1, 1000):
    row_sum = sum(d[i-1])
    #print(row_sum)
    for j in range(10):
        if j == 0:  # 첫번째 열은 그 전 행의 합
            d[i][j] = row_sum
        else:
            d[i][j] = d[i][j-1] - d[i-1][j-1]

for i in range(10):
    result += d[n-1][i]

print(result % 10007)


"""
2차원 배열 선언 - 깊은 복사와 얕은 복사
array = [[0] * 3 for _ in range(3)]  # 기존의 것을 복사하는 것이 아니라, 새롭게 할당
array = [[0] * 3] * 3  # [0,0,0] 은 복사가 되었지만, 실제로는 같은 곳을 참조
겉으로 보기엔 똑같지만 array[0][1] = 1을 넣고 출력해보면 결과가 다르다
이 차이는 객체의 종류로 설명 가능하다
mutable 객체 - 변경 가능 list,set,dictionary 얕은 복사
immutable 갹체 - 변경 불가능 int, float, tuple, str, bool 깊은 복사 
"""
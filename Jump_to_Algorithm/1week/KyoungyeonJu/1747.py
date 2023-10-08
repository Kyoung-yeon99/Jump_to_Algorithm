# 소수&팰린드롬
# 소수 확인하는 함수
""" 시간초과 오류 
def prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    에라토스테네스의 채 활용해서 다시 해보기
"""

num = int(input())
while True:
    if prime_num(num):
        rev_num = int(str(num)[::-1])
        if rev_num == num:
            break

    num = num + 1


print(num)


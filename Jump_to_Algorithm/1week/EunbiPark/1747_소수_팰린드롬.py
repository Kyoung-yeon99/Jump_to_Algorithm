# n 보다 크거나 같고 (1,000,000 이하) 소수이면서 팰린드롬인 수 중 가장 작은수 출력
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True


n = int(input())
min_value = 0

for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if isPrime(i):
            min_value = i
            break

if min_value == 0:
    min_value = 1003001

print(min_value)
'''
# 펠린드롬 확인
def check_pel(num):
    str_num = str(num)

    if len(str_num) % 2 == 0:
        mid = len(str_num) // 2 - 1
    else:
        mid = len(str_num) // 2

    for i in range(mid + 1):
        if str_num[i] != str_num[len(str_num) - 1 - i]:
            return False
        return True
# 소수 확인
def check_sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# main
num = int(input())
ret = 0
for n in range(num, 1000001):
    if check_sosu(n) and check_pel(n):
        print(n)
        break

else:
    print(1003001)
'''

import math

n = int(input())

def isPrime(n): # 소수 판별
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPalindrome(s): # 팰린드롬 판별
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

while(True):
    if isPrime(n) and isPalindrome(str(n)): # 소수이면서 팰린드롬인 n 이상의 가장 작은 숫자
        print(n)
        break
    n += 1


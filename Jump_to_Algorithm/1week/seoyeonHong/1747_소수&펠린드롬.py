import math

n = int(input())

def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

while(True):
    if isPrime(n) and isPalindrome(str(n)):
        print(n)
        break
    n += 1


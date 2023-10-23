import sys

t = int(sys.stdin.readline())

def isPalindrome(s): # 팰린드롬 판별
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def checkWord(s):
    n = len(s)-2
    for i in range(len(s) // 2):
        if s[i] != s[n-i]:
            if isPalindrome(s[i+1:n-i+1]) or isPalindrome(s[i:n-i]): 
                return 1
            else:
                return 2
    return 0

for _ in range(t):
    result = checkWord(sys.stdin.readline())
    if result == 0:
        print(0)
    elif result == 1:
        print(1)
    else:
        print(2)
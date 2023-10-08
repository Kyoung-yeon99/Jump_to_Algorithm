import math

n, k = map(int, input().split())
l = []
count = 0

def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n+1):
    l.append(i)

for i in range(2, n+1):
    if isPrime(i):
        j = 1
        while(i*j < n+1):
            if i*j in l:
                count += 1
                if count == k:
                    print(i*j)
                    break
                l.remove(i*j)            
            j += 1
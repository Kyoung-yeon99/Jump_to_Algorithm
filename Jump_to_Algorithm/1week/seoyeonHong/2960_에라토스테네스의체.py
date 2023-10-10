import math

n, k = map(int, input().split())
l = []
count = 0

def isPrime(n): # 소수 판별
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n+1): # 리스트 l에 2부터 n까지의 수를 저장
    l.append(i)

for i in range(2, n+1): # 2부터 n까지 반복
    if isPrime(i): # i가 소수일 경우
        j = 1
        while(i*j < n+1): # n보다 크지 않은 i의 배수에 대해
            if i*j in l: # 존재하는 숫자일 경우
                count += 1 # 제거 횟수 증가
                if count == k: # k번째로 제거한 숫자일 경우 출력
                    print(i*j)
                    break
                l.remove(i*j) # 리스트에서 숫자 제거
            j += 1
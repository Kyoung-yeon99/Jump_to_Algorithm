# N개의 수 중에서 다른 수 두 개의 합으로 나타낼 수 있는 수의 개수
from collections import defaultdict

N = int(input()) # 수의 개수
A = list(input().split())
d = defaultdict(int) # 숫자의 개수 저장
for i in range(N):
    d[A[i]] += 1 # A[i]가 음수일 수도 있으므로 문자열을 키 값으로 사용

count = 0
for i in range(N):
    d[A[i]] -= 1
    a = int(A[i])
    for j in range(N):
        b = int(A[j])
        if d[A[j]] > 0: # 다른 숫자일 경우
            d[A[j]] -= 1
            if d[str(a - b)] > 0: # 다른 두 숫자를 합해서 나타낼 수 있다면
                count += 1
                d[A[j]] += 1
                break
            d[A[j]] += 1
    d[A[i]] += 1
    
print(count)


# 서로 다른 N개의 자연수의 합이 S일 때, 자연수 N의 최댓값
# (풀이 1) 1부터 s까지의 합은 n(n+1)/2 임을 이용
import math
s = int(input())

# s가 1부터 n까지의 합일 경우
# n(n+1)/2 = s -> n^2+n = 2s -> n^2 < 2s -> n < sqrt(2s)
for n in range(int(math.sqrt(2*s)), 0, -1):
    if n * (n + 1) <= 2 * s: # a(a+1) <= 2s < (a+1)(a+2)
        print(n)
        break

# (풀이 2) 1부터 s까지의 합을 순차적으로 구하며 비교
# s = int(input())
# sum = 0
# for i in range(1, s+1): # s가 1부터 i까지의 합 이하이고 1부터 i+1까지의 합 미만일 경우 i 출력
#     sum += i
#     if sum <= s < sum + i + 1:
#         print(i)
#         break

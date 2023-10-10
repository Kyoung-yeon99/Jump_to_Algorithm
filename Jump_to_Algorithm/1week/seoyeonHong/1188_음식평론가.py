n, m = map(int, input().split())
c = 0 # 칼질 횟수
for i in range(1, m * n):
    if i % m == 0 and i % n == 0: # m과 n의 공약수
        c += 1
print(m - 1 - c)

'''
m * n 개의 조각이 붙어있을 때 m개로 나누는 상황을 가정 : m - 1 번 
원래 n개로 나누어져 있으므로 n의 배수번째 조각은 이미 나누어져 있으므로 제외 : c 번
'''
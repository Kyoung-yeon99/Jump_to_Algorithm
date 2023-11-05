N = int(input())  # 1 <= N <= 1000 이 문제에서는 의미X
A = list(map(int, input().split()))
d = [0] * N

# 이중 for문 range 기준 찾기 어려웠음,,,
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and d[i] < d[j]:  # 기준값 A[i]가 앞의 값들보다 크고 d[i]가 앞의 d[j]보다 작으면
            #print(A[i], A[j], d[i], d[j])
            d[i] = d[j]
            #print(d[i])
    d[i] += 1
    #print("i=", i, "d[i]=", d[i])

print(max(d))

"""
# 리스트 d를 1로 초기화했을 때 
d = [1] * N

for i in range(N):
    for j in range(i):
        if a[i] > a[j]:  # 기준값이 크면
            d[i] = max(d[j]+1, d[i])  # 큰 값 고르기
            
print(max(d))

"""

"""
# 리스트 최소값의 인덱스를 구해서 최소값을 기준으로 크기 비교
# 무조건 최소값보다 크다고 해서 d[i]를 증가하는 건 "가장 긴" 조건 만족 X
d = [1] * N
min_i = A.index(min(A))  
min = A[min_i]

for i in range(1, N):
    if min < A[i]:
        d[i] = d[i-1] + 1
        min = A[i]
        print("min=", min,"i=",i,"A[i]=", A[i], "d[i]=", d[i], "d[i-1]=", d[i-1])
    else:
        d[i] = d[i-1]
        print("min=", min, "i=",i,"A[i]=", A[i], "d[i]와 d[i-1]=", d[i - 1])

print(d[-1])
"""

# 합이 s가 되는 부분수열의 개수(공집합X), s가 0인 경우 주의
n, s = map(int, input().split()) # 정수의 개수, 부분수열의 합
seq = list(map(int, input().split())) # 수열
sum = [0] # 부분수열의 합 저장
seq.sort() # 오름차순 정렬

for i in range(n): # 수열의 i번째를 포함할 경우 계산
    sum_len = len(sum)
    for j in range(sum_len): # 0~i-1번째 부분수열 합 + i번째 수
        sum.append(sum[j] + seq[i])

print(sum[1:].count(s)) # 공집합 제외, 합이 s인 부분수열 개수 출력


# 반례
# 5 5
# 3 2 1 2 3
# ans: 5

# 시간초과
# n, s = map(int, input().split()) # 정수의 개수, 부분수열의 합
# seq = list(map(int, input().split())) # 수열
# sum = [0] # 부분수열의 합 저장

# for i in range(n):
#     sum_len = len(sum)
#     for j in range(sum_len):
#         num = sum[j] + seq[i]
#         if num not in sum:
#             sum.append(num)

# print(sum.count(s))
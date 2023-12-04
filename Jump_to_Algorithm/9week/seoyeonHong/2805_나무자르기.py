# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
n, m = map(int, input().split()) # 나무의 수, 가져가려는 나무의 길이
t = list(map(int, input().split())) # 나무의 높이
h = 0
low, high = 0, max(t)
cut = high // 2
while low <= high:
    sum = 0
    for i in range(n):
        if t[i] > cut:
            sum += t[i] - cut
            if sum > m: # 시간 초과 해결
                break
    if sum >= m: # 필요한 양보다 많을 경우
        low = cut + 1
        break
    else: # 필요한 양보다 적을 경우
        high = cut - 1
    cut = (high + low) // 2

print(cut)

# 시간초과
# n, m = map(int, input().split()) # 나무의 수, 가져가려는 나무의 길이
# t = list(map(int, input().split())) # 나무의 높이
# t.sort() # 오름차순 정렬
# h = t.pop() - 1 # 가장 큰 나무의 높이 - 1
# sum = 1
# c = 1 
# while sum < m:
#     while t[-1] == h:
#         t.pop()
#         c += 1
#     sum += c
#     h -= 1

# print(h)
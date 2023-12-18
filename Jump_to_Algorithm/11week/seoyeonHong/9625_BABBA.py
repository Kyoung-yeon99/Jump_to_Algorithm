# k번째 a의 개수: k-1번째 a의 개수, k번째 b의 개수: k-1번째 a의 개수 + b의 개수
k = int(input()) # 버튼 조작 횟수
a, b = 1, 0 # a, b의 개수
for _ in range(k):
    a, b = b, a + b 
print(a, b)
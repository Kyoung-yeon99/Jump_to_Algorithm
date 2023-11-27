n, k = map(int, input().split())
h = list(map(int, input().split()))  # 원생들 키
diff = []  # 키 차이

# 키 차이 구하기
for i in range(1, n):
    diff.append(h[i] - h[i - 1])

# 키 차이를 오름차순 정렬
diff.sort()

ans = 0  # 티셔츠 최소 비용

# 학생의 수에서 조의 개수를 뺀만큼 반복해 원생의 키 차이수 -> 티셔츠 비용 구함
for j in range(n - k):
    ans += diff[j]
print(ans)

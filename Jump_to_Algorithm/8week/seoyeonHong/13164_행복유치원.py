# k개의 조별 키 차이 합이 최소
n, k = map(int, input().split()) # 원생의 수, 조의 개수
h = list(map(int, input().split())) # 원생들의 키(오름차순)

diff = [] # 키 차이
for i in range(n-1):
    diff.append(h[i+1] - h[i])
diff.sort() # 키 차이를 오름차순으로 정렬

print(sum(diff[:n-k])) # 가장 큰 차이 k-1개는 제외해도 됨
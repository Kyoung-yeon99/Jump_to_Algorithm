# 가장 많은 고층 빌딩이 보이는 고층 빌딩 찾고 거기서 보이는 빌딩의 수 출력하기
# 고층빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선문이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다
N = int(input())  # 1 <= N <= 50
heights = list(map(int, input().split()))  # 1,000,000,000보다 작거나 같은 자연수
answer = [0]*N

for i in range(N):
    min_s = float('inf')
    for j in range(i-1, -1, -1):  # 왼쪽
        s = (heights[i] - heights[j]) / (i - j)
        if s < min_s:
            min_s = s
            answer[i] += 1

    max_s = float('-inf')
    for j in range(i+1, N):  # 오른쪽
        s = (heights[j] - heights[i]) / (j - i)
        if s > max_s:
            max_s = s
            answer[i] += 1

print(max(answer))

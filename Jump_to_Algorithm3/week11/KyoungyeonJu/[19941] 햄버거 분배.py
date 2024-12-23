# 식탁 길이 N, 햄버거를 선택할 수 있는 거리 K
# 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수 구하기
# 시간 0.5초, 메모리 256MB
# 그냥 구현..? 스택?

N, K = map(int, input().split())  # 1 <= N <= 20000,  1 <= k <= 10
HP = list(input())  # P(사람)와 H(햄버거)
answer = 0

i = 0
while i < N:
    if HP[i] == "P":
        for j in range(-K, K+1):
            if 0 <= i+j < N and HP[i+j] == "H":
                answer += 1
                HP[i+j] = answer
                break
    i += 1

print(answer)
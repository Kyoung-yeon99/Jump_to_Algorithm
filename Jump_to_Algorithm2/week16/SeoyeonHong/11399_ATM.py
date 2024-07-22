# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램
N = int(input()) # 사람의 수
P = list(map(int, input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간
P.sort()
T = [0]
for i in range(N):
    T.append(P[i] + T[i])
print(sum(T))
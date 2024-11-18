import math

H, W, N, M = map(int, input().split())
print(math.ceil(H / (1+N)) * math.ceil(W / (1+M))) # 한 행에 앉을 수 있는 사람 수 * 한 열에 앉을 수 있는 사람 수
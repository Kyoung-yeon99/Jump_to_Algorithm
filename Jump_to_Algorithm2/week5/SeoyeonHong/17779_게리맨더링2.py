# 오답...
# 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
import sys
import heapq

input = sys.stdin.readline
N = int(input()) # 재현시의 크기, 5~20
A = [] # r행 c열의 인구는 A[r][c], 1~100

total_population = 0
difference = []

for _ in range(N):
    row = list(map(int, input().split()))
    total_population += sum(row)
    A.append(row)

def calculate(x, y, d1, d2):
    s = [[5 for _ in range(N)] for _ in range(N)]
    p = [0 for _ in range(5)] # 선거구별 인구

    for r in range(1, N+1):
        for c in range(1, N+1):
            if 1 <= r < x+d1 and 1 <= c <= y:
                if r+c <= x+y-1:
                    s[r-1][c-1] = 1
                    p[0] += A[r-1][c-1]
            elif 1 <= r <= x+d2 and y < c <= N:
                if r-c <= x-y-1:
                    s[r-1][c-1] = 2
                    p[1] += A[r-1][c-1]
            elif x+d1 <= r <= N and 1 <= c < y-d1+d2:
                if r-c > x+d1-y+d1:
                    s[r-1][c-1] = 3
                    p[2] += A[r-1][c-1]
            elif x+d2 < r <= N and y-d1+d2 <= c <= N:
                if r+c > x+y+d1+1:
                    s[r-1][c-1] = 4
                    p[3] += A[r-1][c-1]
    # print()
    # for row in s:
    #     print(*row)
    # print()
   
    p[4] = total_population - sum(p) # 5번 선거구
    # print(p, max(p), min(p))
    return  max(p) - min(p) # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값

# calculate(2, 4, 2, 2)
# calculate(2, 5, 3, 2)
# calculate(4, 3, 1, 1)

for d1 in range(1, N): # 1 <= d1, d2 -> 1 <= d1 < N
    for d2 in range(1, N-d1): # 1 <= d2 <= N-d1
        for x in range(1, N-d1-d2+1): # 1 <= x < N-d1-d2
            for y in range(1+d1, N-d2+1): # 1+d1 < y < N-d2
                heapq.heappush(difference, calculate(x, y, d1, d2))

print(difference)
print(heapq.heappop(difference))

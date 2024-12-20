from sys import stdin
# 1<= K <=10
N,K = map(int,stdin.readline().rstrip().split())
#(인덱스, 햄버거 = 1), (인덱스, 사람 = 0)
arr = [1 if s == 'H' else 0 for s in stdin.readline().rstrip()]
max_num = 0
#1부터 10까지 K돌면서 최대수 구하기
for i in range(N):
    if arr[i] == 0:
        #왼쪽->오른쪽 탐색
        for j in range(max(0, i-K), min(N, i+K+1)):
            if arr[j] == 1:
                max_num+=1
                arr[j] = -1
                break

print(max_num)

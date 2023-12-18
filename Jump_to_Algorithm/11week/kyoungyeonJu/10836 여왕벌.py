import sys
input = sys.stdin.readline

m, n = map(int, input().split())
larva = [1 for _ in range(2*m-1)]
for _ in range(n):
    zero, one, two = map(int, input().split())  # 0의 개수, 1의 개수, 2의 개수
    # 모든 입력에서 제일 왼쪽에서 위쪽으로 그리고 오른쪽으로 읽은 값들은 감소하지 않는 형태
    for i in range(zero, zero+one):  # 애벌레 크기 1 증가
        larva[i] += 1
    for i in range(zero+one, zero+one+two):  # 애벌레 크기 2 증가
        larva[i] += 2

for i in range(m):
    for j in range(m):
        if j == 0:  # 맨 왼쪽 열
            print(larva[m-(i+1)], end=" ")  # i=0,j=0 값 == larva[m-1]
        else:  # 나머지 애벌레들은 항상 자신의 위쪽 애벌레만큼 커진다
            print(larva[m+j-1], end=" ")  # i=1,j=1 값 == i=0,j=1 == larva[m]
    print()

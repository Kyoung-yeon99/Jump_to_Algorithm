import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))[:n-1]  # 마지막 오일 가격은 의미 없음

if set(oil) == {1}:  # 모든 주유소의 리터당 가격이 1인 경우
    print(sum(dis))
else:
    # 자신보다 작은 오일 가격 나오기 전까지 길이 더해서 추가
    answer, min_, min_i = oil[0]*dis[0], oil[0], 0
    for i in range(n-2):  # i와 i+1를 비교하기 때문에 range(n-2)까지
        if min_ > oil[i+1]:
            min_, min_i = oil[i+1], i+1
        answer += min_*dis[i+1]

    print(answer)



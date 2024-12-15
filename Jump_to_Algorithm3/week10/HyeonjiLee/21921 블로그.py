from sys import stdin
N, X = map(int, stdin.readline().rstrip().split())
visitors = list(map(int, stdin.readline().rstrip().split()))

sum_visitors = []
cur_sum = 0
for i in range(N):
    if i < X:
        cur_sum += visitors[i]
    else:
        sum_visitors.append(cur_sum)
        cur_sum -= visitors[i-X]
        cur_sum += visitors[i]

sum_visitors.append(cur_sum) #맨마지막 추가

if max(sum_visitors)==0:
    print("SAD")
else:
    answer = max(sum_visitors)
    print(answer)
    answer_cnt = sum_visitors.count(answer)
    print(answer_cnt)
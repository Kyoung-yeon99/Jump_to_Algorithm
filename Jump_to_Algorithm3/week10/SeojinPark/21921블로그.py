import sys
input=sys.stdin.readline

n, x = map(int,input().split())
visit=list(map(int,input().split()))
visit_cnt=sum(visit[:x])
max_visit=visit_cnt
day_cnt=1

for i in range(n-x):
    visit_cnt += visit[i+x]-visit[i]
    if visit_cnt>max_visit:
        max_visit=visit_cnt
        day_cnt=1
    elif visit_cnt==max_visit:
        day_cnt += 1

if max_visit==0:
    print('SAD')
else:
    print(max_visit)
    print(day_cnt)
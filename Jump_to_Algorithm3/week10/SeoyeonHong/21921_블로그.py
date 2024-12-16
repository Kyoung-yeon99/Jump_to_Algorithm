from collections import defaultdict

N, X = map(int, input().split())
view = list(map(int, input().split())) # 방문자 수
count = defaultdict(int)
if max(view) == 0:
    print("SAD")
else:
    total_view = sum(view[0:X])
    count[total_view] += 1
    for i in range(N-X):
        total_view += view[i+X]-view[i]
        count[total_view] += 1
    print(max(count))
    print(count[max(count)])
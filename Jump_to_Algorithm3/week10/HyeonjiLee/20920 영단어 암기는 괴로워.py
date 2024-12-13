from sys import stdin
from collections import defaultdict

N,M = map(int, stdin.readline().rstrip().split())
dic = defaultdict(int) #기본값 0으로
for _ in range(N):
    word = stdin.readline().rstrip()
    #M보다 짧으면 안외움
    if len(word) < M:
        continue

    dic[word]+=1

sorted_dic = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for k,v in sorted_dic:
    print(k)
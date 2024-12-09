from collections import defaultdict

word = input()
dic = defaultdict(int)

for i in word:
    dic[i.upper()] += 1

if len(dic) == 1:  # 알파벳이 하나인 경우
    print(list(dic.keys())[0])
    exit(0)

d = sorted(dic.items(), key=lambda x: -x[1])
if d[0][1] == d[1][1]:
    print("?")
else:
    print(d[0][0])
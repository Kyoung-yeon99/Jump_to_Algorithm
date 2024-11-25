from sys import stdin
N, K = map(int, stdin.readline().rstrip().split())

medal_dic = {}
for _ in range(N):
    nation, g, s, b = map(int, stdin.readline().rstrip().split())
    add_medals = [g,s,b]
    medal_dic[nation] = add_medals

orders = sorted(list(medal_dic.items()), key = lambda x: (-x[1][0],-x[1][1],-x[1][2]))
id = orders.index((K,medal_dic[K]))
answer = 1
while True:
    if id < 0:
        break
    if medal_dic[K] != orders[id][1]:
        answer += 1

    id-=1
print(answer)

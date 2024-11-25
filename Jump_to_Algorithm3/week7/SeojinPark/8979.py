nation, key = map(int, input().split())
nation_medal=[]
for i in range(nation):
    lst = list(map(int, input().split()))
    nation_medal.append(lst)

nation_medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [nation_medal[i][0] for i in range(nation)].index(key)
for i in range(nation):
    if nation_medal[idx][1:] == nation_medal[i][1:]:
        print(i+1)
        break

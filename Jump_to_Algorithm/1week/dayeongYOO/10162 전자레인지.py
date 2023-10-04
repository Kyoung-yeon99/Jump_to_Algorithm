t = int(input())
btn = [300, 60, 10]
cnt = {}

for b in btn:
    click_cnt = t // b
    cnt[b] = click_cnt
    t -= (click_cnt * b)

if t == 0:
    for k, v in cnt.items():
        print(v, end=' ')
else:
    print(-1)

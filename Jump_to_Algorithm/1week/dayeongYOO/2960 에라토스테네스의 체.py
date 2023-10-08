import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0  # 순서 카운트

# 2부터 n 까지
lst = [i for i in range(2, n + 1)]

while len(lst) != 0:
    # 가장 작은 수 : p
    min_num = lst[0]
    baesu_lst = []

    for j in range(len(lst)):  # 2~7
        if lst[j] % lst[0] == 0:
            # lst.remove(lst[j])
            baesu_lst.append(lst[j])
            cnt += 1
            if cnt == k:
                print(baesu_lst[-1])
                break
    if cnt == k:
        break
    lst = [x for x in lst if x not in baesu_lst]

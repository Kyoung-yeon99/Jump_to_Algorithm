from sys import stdin
N, M = map(int,stdin.readline().split())

power_dic = {}
for _ in range(N):
    t, p = stdin.readline().split()
    if int(p) in power_dic: #중복 X
        continue
    else:
        power_dic[int(p)] = t

input_list = []
for _ in range(M):
    input_list.append(int(stdin.readline()))

#각 전투력 리스트에 대해 칭호 이분탐색
def binary_search(arr, st, start, end):
    if start > end:
        return start
    mid = (start+end)//2

    if arr[mid] == st:
        return mid
    elif arr[mid] < st:
        return binary_search(arr,st, mid + 1, end)
    elif arr[mid] > st:
        return binary_search(arr, st, start, mid - 1)

power_list = list(power_dic.keys())

for inputs in input_list:
    id = binary_search(power_list, inputs, 0, len(power_list) - 1)
    print(power_dic[power_list[id]])

# 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램
N = int(input())
status = list(map(int, input()))
target = list(map(int, input()))
INF = int(1e9)

def change(count, status, target):
    for i in range(1, N):
        if status[i-1] == target[i-1]: # 바로 직전 인덱스의 전구를 비교하여 스위치를 누를지 결정
            continue
        count += 1
        for j in range(i-1, i+2):
            if j < N:
                status[j] = 1 - status[j]

    if status == target:
        return count
    else:
        return INF

res1 = change(0, status.copy(), target) # 첫번째 스위치를 누른 경우
status[0] = 1 - status[0]
status[1] = 1 - status[1]
res2 = change(1, status.copy(), target) # 첫번째 스위치를 누르지 않은 경우
min_res = min(res1, res2) # 스위치를 누른 횟수의 최솟값

print(min_res if min_res != INF else -1)

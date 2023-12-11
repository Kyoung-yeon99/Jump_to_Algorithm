from heapq import *

n = int(input())
student_num = int(input())
student = list(map(int, input().split()))
pick = list()

for idx, num in enumerate(student):
    temp = list()
    flag = 0

    while pick:
        cnt, old_idx, std_num = heappop(pick)
        cnt += 1 if std_num == num else 0
        heappush(temp, (cnt, old_idx, std_num))
        flag += std_num == num

    if not flag and len(temp) >= n:
        heappop(temp)
    if not flag:
        heappush(temp, (0, idx, num))
    pick = temp

answer = [x[-1] for x in pick]
answer.sort()

print(*answer)
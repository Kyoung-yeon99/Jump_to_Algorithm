n = int(input())
count = [0] * 10001  # 문제에서 최대 수는 10000임.

for _ in range(n):
    input_num = int(input())
    count[input_num] += 1  # counting sort
for i in range(len(count)):
    for j in range(count[i]):
        print(i)

# https://www.acmicpc.net/problem/1406

input_str = list(input())
m = int(input())  # 명령어 개수

# 커서 배열
temp = []
for _ in range(m):
    command = input().split()

    if 'L' in command:
        if len(input_str) == 0: continue  # 맨 앞이라면 무시
        temp.append(input_str.pop())

    elif 'D' in command:
        if len(temp) == 0: continue  # 맨 뒤라면 무시
        input_str.append(temp.pop())

    elif 'B' in command:
        if len(input_str) == 0: continue  # 맨 앞이라면 무시
        input_str.pop()
    elif command[0] == 'P':
        input_str.append(command[1])

input_str += temp[::-1]
print(*input_str, sep='')

# 시간 초과 발생...
string = list(input())
num = int(input())
cursor = len(string)

for _ in range(num):
    arr = list(input().split())
    if arr[0] == 'P':
        string.insert(cursor, arr[1])
        cursor += 1
    elif arr[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif arr[0] == 'D':
        if cursor != len(string):
            cursor += 1
    elif arr[0] == 'B':
        if cursor != 0:
            string.remove(string[cursor-1])
            cursor -= 1


print(''.join(string))




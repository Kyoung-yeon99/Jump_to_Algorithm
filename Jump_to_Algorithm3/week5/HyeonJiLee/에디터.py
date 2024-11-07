from sys import stdin
left = list(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
right = []
#시간초과 별짓 다해도 안되어서 구글링 -> 표준입출력 라이브러리 sys.stdin
#커서를 기준으로 왼쪽/오른쪽 스택 값 변경. 좌우 이동하면서 스택 push/pop
for _ in range(M):
    command = stdin.readline().rstrip().split()

    if command[0] == 'L' and left: #커서 왼쪽 이동
        right.append(left.pop())
    elif command[0] == 'D' and right: #커서 오른쪽 이동
        left.append(right.pop())
    elif command[0] == 'B' and left: #문자 제거
        left.pop()
    elif command[0] == 'P': #문자 추가
        left.append(command[1])

print("".join(left+right[::-1]))

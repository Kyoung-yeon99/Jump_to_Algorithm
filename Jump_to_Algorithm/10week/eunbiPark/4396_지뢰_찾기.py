n = int(input())

graph1 = list(input() for _ in range(n))
graph2 = list(input() for _ in range(n))
answer = [['.'] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def findBoom():
    for i in range(n):
        for j in range(n):

            if graph1[i][j] == '.' and graph2[i][j] == 'x':
                boom = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n: # 리스트 좌표 벗어났을때
                        continue

                    if graph1[nx][ny] == '*':
                        boom += 1
                answer[i][j] = boom

            if graph1[i][j] == '*' and graph2[i][j] == 'x':
                makeFail()


def makeFail():
    global answer
    for i in range(n):
        for j in range(n):
            if graph1[i][j] == '*':
                answer[i][j] = '*'


findBoom()
for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()
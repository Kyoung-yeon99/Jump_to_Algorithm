# 입력
n = int(input())
board = []
# 출력
answer = []

for i in range(n):
    board.append(list(map(int, input())))


# print(board)

def quad_tree(x, y, size):
    first_node = board[x][y]

    for i in range(x, x + size):  # 탐색
        for j in range(y, y + size):
            # 0, 1이 섞여있다면
            if first_node != board[i][j]:
                answer.append('(')  # 쪼개질때마다 괄호 추가.
                size = size // 2  # 사분면 당 크기
                quad_tree(x, y, size)  # 1사분면
                quad_tree(x, y + size, size)  # 2사분면
                quad_tree(x + size, y, size)  # 3사분면
                quad_tree(x + size, y + size, size)  # 4사분면
                answer.append(')')

                return answer

    if first_node == 1:  # 해당 사분면의 수가 모두 1이라면
        answer.append('1')
    if first_node == 0:  # 해당 사분면의 수가 모두 0이라면
        answer.append('0')
    return answer


print(''.join(quad_tree(0, 0, n)))

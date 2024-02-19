# 정사각형 색종이
# 규칙에 따라 잘라 하얀색, 파란색 색종이 만듦.
# 모두 같은 색이 아니라면 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순서로 자름(1/2)
# 모두 같은 색일 때까지 반복
# 하나의 정사각형 칸이면 종료

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 흰, 파 색
blue, white = 0, 0


def paper(board, n):
    global blue, white

    # 같은 색?
    # 모두 파란색: n**2, 모두 하얀색: 0
    color = 0
    for r in board:
        color += sum(r)
    if color == n ** 2:
        blue += 1
        return
    elif color == 0:
        white += 1
        return
    # 모두 같은 색이 아니라면 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순서로 자름(1/2)
    else:
        half = n // 2
        paper([row[:half] for row in board[:half]], half)  # top_left
        paper([row[half:] for row in board[:half]], half)  # top_right
        paper([row[:half] for row in board[half:]], half)  # under_left
        paper([row[half:] for row in board[half:]], half)  # under_right


# 함수 실행
paper(board, n)
print(white)
print(blue)

# for b in board:
#     # 가로 절반
#     print(b[0~half:half]) # 어떻게 가로, 세로의 절반씩 자를까? # 위 코드 참고
# https://ryong9rrr.github.io/boj2630/
#
#     # 세로 절반
#     print(b[half:])

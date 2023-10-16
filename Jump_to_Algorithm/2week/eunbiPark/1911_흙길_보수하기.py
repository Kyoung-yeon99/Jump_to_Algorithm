n, l = map(int, input().split()) # 웅덩이 개수, 널빤지 길이
board = [
    list(map(int, input().split())) # 웅덩이 시작 to 끝
    for _ in range(n)
]

board.sort()
total_cnt = 0 # 널빤지의 개수
plank = board[0][0] # 널판지 시작

for start, end in board:
    if plank > end:
        continue

    elif plank < start:
        plank = start

    dist = end - plank # 마지막 널빤지와 웅덩이 사이 거리
    remainder = 1 # flag 변수

    # 딱 맞아 떨어짐
    if dist % l == 0:
        remainder = 0

    # 몫 + 남아떨어지지 않으니 그 부분 개수(1)
    cnt = dist // l + remainder
    plank += cnt * l # 널빤지의 시작 지점 변경
    total_cnt += cnt

print(total_cnt)

'''
# 시간 초과 
idx = 0 # 마지막 널판지의 위치

for start, end in board:
    if start > end:
        continue

    # 이전 널빤지가 새로운 웅덩이의 시작지점을 덮을 경우
    if idx > start:
        start = idx # 시작 위채 재조정

    # 널판지 개수 세기
    while start < end:
        start += l # start 지점 갱신 (널빤지 썼으니 뒤로)
        cnt += 1 # 널빤지 개수 갱신
    idx = start # 널판지의 마지막 위치로 idx 이동

print(cnt)
'''

'''
for idx, b in enumerate(board):
    print(b)
    # 지금 필요한 널판지 개수
    p_cnt = math.ceil((b[1] - b[0]) / l)
    # print(p_cnt)
    cnt += p_cnt
    remain_value = (b[1] - b[0]) % l

    if remain_value: # 나머지가 있으면
        # 널판지 않에 다음 웅덩이가 있다면
        if idx < len(board) - 1 and remain_value + l >= board[idx + 1][0]:
            board[idx + 1][0] = b[1] + (l - remain_value)

        # if idx < len(board) -1  and remain_value - 1 + l >= board[idx+1][0]:
            # cnt += 1
            # board[idx+1][0] = b[1] + (l - remain_value) -1

print(cnt)
'''

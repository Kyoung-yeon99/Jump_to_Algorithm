# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    di = {"E": 0, "W": 1, "S": 2, "N": 3}
    R, C = len(park), len(park[0]) # 행, 열의 수
    r, c = 0, 0
    flag = False # 출발점을 찾을 경우 True
    for row in range(R):
        for column in range(C):
            if park[row][column] == "S":
                r, c = row, column # 출발 위치 저장
                flag = True
                break
        if flag:
            break
                
    for route in routes:
        movable = True # 명령 수행 가능 여부
        op, count = route.split() # 이동할 방향, 칸의 수
        count = int(count)
        nr, nc = r, c
        for _ in range(count):
            nr, nc = nr + dr[di[op]], nc + dc[di[op]]
            if 0 <= nr < R and 0 <= nc < C and park[nr][nc] != "X": # 갈 수 있는 곳이라면
                continue
            else: # 갈 수 없는 곳이라면
                movable = False
                break
        if movable: # 명령을 수행할 수 있으면
            r, c = nr, nc # 이동
            
    answer = [r, c]
    return answer
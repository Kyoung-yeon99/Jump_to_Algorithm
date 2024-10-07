# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# 처음 걸어본 길의 길이
def solution(dirs):
    answer = 0
    R, C = 11, 11
    index = {'U': 0, 'R': 1, 'L': 2, 'D': 3}
    dr, dc = [-1, 0, 0, 1], [0, 1, -1, 0]
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)] # 좌표 방문 여부
    
    r, c = 5, 5 # 시작 위치
    for d in dirs:
        i = index[d]
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C: # 좌표평면 범위 안으로 이동할 경우
            if not visited[r][c][i]: # 처음 방문하는 길이라면
                visited[r][c][i] = True # 이전 좌표에서 다음 좌표로 이동하는 경로 방문 처리
                visited[nr][nc][3-i] = True # 다음 좌표에서 이전 좌표로 이동하는 경로 방문 처리
                answer += 1 # 처음 가는 길의 길이 +1
            r, c = nr, nc # 다음 좌표로 이동

    return answer
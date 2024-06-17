# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = []
    X, Y = len(wallpaper), len(wallpaper[0]) # 바탕화면 행, 열의 크기
    lux, luy, rdx, rdy = X, Y, 0, 0
    for x in range(X):
        if '#' in wallpaper[x]: # 파일이 있으면
            for y in range(Y):
                if wallpaper[x][y] == '#':
                    # 가장 왼쪽, 오른쪽에 있는 파일의 열 저장
                    luy = min(luy, y)
                    rdy = max(rdy, y)
            # 가장 위쪽, 아래쪽에 있는 파일의 행 저장
            lux = min(lux, x)
            rdx = max(rdx, x)
    answer = [lux, luy, rdx+1, rdy+1]
    return answer
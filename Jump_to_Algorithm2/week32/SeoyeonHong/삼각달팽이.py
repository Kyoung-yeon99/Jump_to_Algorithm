# https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=python3

def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    
    def fill_triangle(r, c, s, l):       
        for i in range(r, r+l): # 왼쪽
            arr[i][c] = s
            s += 1
        l -= 1
        r += l
        for _ in range(l): # 아래
            c += 1
            arr[r][c] = s
            s += 1
        l -= 1
        for _ in range(l): # 오른쪽
            r, c = r-1, c-1
            arr[r][c] = s
            s += 1
        l -= 1

        if l > 0: # 다음 삼각형 채우기
            fill_triangle(r+1, c, s, l)
            
    fill_triangle(0, 0, 1, n)
    
    for row in arr:
        answer += row
        
    return answer
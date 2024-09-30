# https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=python3

# 쿼드압축 후 0과 1의 개수 구하기
def solution(arr):
    answer = [0, 0] # 0과 1의 개수
    
    def compress(r, c, n): # 압축하고자 하는 영역의 시작 행, 열, 크기
        
        if n == 1: # 영역의 크기가 1이라면
            answer[arr[r][c]] += 1 # 해당 숫자 반환
            return

        quad = [] # 압축하고자 하는 숫자들의 배열
        for i in range(n):
            quad += arr[r+i][c:c+n]
            
        if len(set(quad)) == 1: # 모두 같은 수로 이루어져 있다면
            answer[quad[0]] += 1 # 0 또는 1의 개수 +1
        else: # 4개의 영역으로 나누어 압축
            n //= 2
            compress(r, c, n)
            compress(r, c+n, n)
            compress(r+n, c, n)
            compress(r+n, c+n, n)
        
        return
        
    compress(0, 0, len(arr[0])) # 배열 압축
    
    return answer
#https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=python3

def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows):
        num = i * columns + 1
        matrix.append([j for j in range(num, num + columns)])
        
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        before = matrix[x1+1][y1]
        temp = 0
        min_num = rows * columns
        for i in range(y1, y2+1): # 위쪽
            temp = matrix[x1][i]
            min_num = min(min_num, temp)
            matrix[x1][i] = before
            before = temp
        
        for i in range(x1+1, x2+1): # 오른쪽
            temp = matrix[i][y2]
            min_num = min(min_num, temp)
            matrix[i][y2] = before
            before = temp
            
        for i in range(y2-1, y1-1, -1): # 아래쪽
            temp = matrix[x2][i]            
            min_num = min(min_num, temp)
            matrix[x2][i] = before
            before = temp
            
        for i in range(x2-1, x1, -1): # 왼쪽
            temp = matrix[i][y1]
            min_num = min(min_num, temp)
            matrix[i][y1] = before
            before = temp
            
        answer.append(min_num)
            
    return answer
def quard(arr, row, col, num, answer):
    first = arr[row][col]  # 맨 첫번째 원소부터 비교
    is_quard = True  # 모두 같은지 확인

    for r in range(row, row + num):
        for c in range(col, col + num):
            if arr[r][c] != first:  # 원소가 다르면 break
                is_quard = False
                break
        if not is_quard:
            break
    if is_quard:  # 원소 다 같으면
        if first == 1:
            answer[1] += 1
        else:
            answer[0] += 1
    else:
        # 이후 4개 영역 나눠서 재귀 돌리기
        quard(arr, row, col, num // 2, answer)  # 왼쪽 위
        quard(arr, row, col + num // 2, num // 2, answer)  # 왼쪽 아래
        quard(arr, row + num // 2, col, num // 2, answer)  # 오른쪽 위
        quard(arr, row + num // 2, col + num // 2, num // 2, answer)  # 오른쪽 아래

def solution(arr):
    zero, one = 0,0
    answer = [zero,one]
    quard(arr,0,0,len(arr),answer) #맨 왼쪽 위부터 시작
    return answer

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

# 동일한 가짓수의 토핑이 올라가도록 롤케이크를 자르는 방법의 수
def solution(topping):
    answer = 0
    topping_set = set(topping) # 토핑의 종류
    pieceA = {t: 0 for t in topping} 
    for t in topping:
        pieceA[t] += 1
    cntA = len(pieceA) # 조각A의 토핑 종류 수
    pieceB = {t: 0 for t in topping}
    cntB = 0 # 조각B의 토핑 종류 수
    
    for t in topping:
        pieceA[t] -= 1
        if pieceA[t] == 0: # 조각A의 토핑 종류 감소
            cntA -= 1
        if pieceB[t] == 0: # 조각B의 토핑 종류 증가
            cntB += 1
        pieceB[t] += 1
    
        if cntA == cntB: # 토핑 종류 수가 같을 경우
            answer += 1
        elif cntA < cntB: # 조각B의 토핑 종류수가 더 많아질 경우 종료
            break
    
    return answer
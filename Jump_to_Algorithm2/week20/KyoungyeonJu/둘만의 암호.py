# chr(숫자) -> 문자열 
# ord(알파벳) -> 아스키코드(10진수)
def solution(s, skip, index):
    answer = ''
    alphabets = []

    # ord('a') = 97, ord('z') = 122
    for i in range(97, 123):
        if chr(i) in skip:
            continue
        alphabets.append(chr(i))   

    for i in s:
        idx = alphabets.index(i) + index
        idx %= len(alphabets)
        answer += alphabets[idx]

    return answer


"""
# 런타임 오류 발생 코드
idx -= len(alphabets)는 단순히 한 번만 idx값 수정
만약, idx가 len(alphabets)의 배수 이상일 경우, 런타임 에러(인덱스 에러) 발생 
e.g) idx = 43, len(alphabets) = 21   
idx = 43 - 21 = 22 여전히 21보다 크다
이를 해결하기 위해 idx를 리스트 길이로 나눈 "나머지 값 연산" 사용

for i in s:                    
    idx = alphabets.index(i) + index
    if idx > len(alphabets) - 1:
        idx -= len(alphabets)  
        
    answer += alphabets[idx] 
"""
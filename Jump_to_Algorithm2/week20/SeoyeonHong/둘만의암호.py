# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    # 알파벳 목록
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for sk in skip: # skip에 해당하는 알파벳 제거
        a.remove(sk)
        
    for i in range(len(s)):
        j = a.index(s[i])
        j = (j + index) % len(a) # s[i]에서 index만큼 뒤에 있는 알파벳 인덱스
        answer += a[j]
        
    return answer
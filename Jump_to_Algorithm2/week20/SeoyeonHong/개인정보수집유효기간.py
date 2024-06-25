# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    periods = {} # {약관 종류: 유효 기간}
    ty, tm, td = today.split('.')
    ty, tm, td = int(ty), int(tm), int(td)
    
    for term in terms:
        t, p = term.split()
        periods[t] = int(p)
        
    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term = privacy.split()
        y, m, d = date.split('.')
        y, m, d = int(y), int(m), int(d)
        period = periods[term]
        pm = (ty * 12 * 28 + tm * 28 + td - (y * 12 * 28 + m * 28 + d)) / 28 # 지난 달 수
        if pm >= period:
            answer.append(i+1)
            
    return answer
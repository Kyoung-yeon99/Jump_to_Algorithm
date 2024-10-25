def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        c = citations[i]
        if c < i + 1:
            return i

    return len(citations)


"""
def solution(citations):
    answer = len(citations)  # 최대 h-index는 논문의 개수
    citations.sort(reverse=True)

    for i in range(len(citations)):
        c = citations[i]
        if c <= i+1:  # i+1번 이상 인용된 논문이 i+1편 이상인 경우 
            answer = max(i, c)  
            break

    return answer


"""

"""
    answer = []
    citations.sort(reverse=True)

    for i in range(len(citations)):
        answer.append(min(i+1, citations[i]))

    return max(answer)
"""
def solution(survey, choices):
    answer = ''
    # 타입 이름 : 점수
    type = {
        'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0
    }

    # 점수 등록
    for idx, c in enumerate(choices):
        score = c - 4

        if score < 0:  # 앞 유형
            type[survey[idx][0]] += -score
        elif score > 0:  # 뒷 유형
            type[survey[idx][1]] += score

    # 결과 등록
    if type['R'] > type['T']:
        answer += 'R'
    elif type['R'] < type['T']:
        answer += 'T'
    else: # if 문과 합칠 수 있음
        answer += 'R'

    if type['C'] > type['F']:
        answer += 'C'
    elif type['C'] < type['F']:
        answer += 'F'
    else:
        answer += 'C'

    if type['J'] > type['M']:
        answer += 'J'
    elif type['J'] < type['M']:
        answer += 'M'
    else:
        answer += 'J'

    if type['A'] > type['N']:
        answer += 'A'
    elif type['A'] < type['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer

'''
# sol2)
# survey	choices	result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"

def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices): # zip으로 한 번에 처리 
        if A not in my_dict.keys():
            A = A[::-1] # 거꾸로 돌림
            my_dict[A] -= B-4 # 없으면 음수 
        else:
            my_dict[A] += B-4 # 있으면 양수 

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result


'''
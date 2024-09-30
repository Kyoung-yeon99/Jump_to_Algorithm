def solution(s):
    answer, new_s = [], []
    s = s[2:-2].split('},{')  # 앞{{ 뒤}} 제거 후, '},{' 분리

    for ss in s:
        new_s.append(set(map(int, ss.split(','))))

    new_s.sort(key=lambda x: len(x))
    answer.extend(new_s[0])

    for sss in new_s[1:]:  # answer에 없는 하나의 원소를 찾아서 answer에 추가
        #  1. set 데이터타입의 차집합 활용
        # answer.append((sss - set(answer)).pop())
        #  2. filter 와 lambda 활용
        answer.extend(list(filter(lambda x: x not in set(answer), sss)))

    return answer
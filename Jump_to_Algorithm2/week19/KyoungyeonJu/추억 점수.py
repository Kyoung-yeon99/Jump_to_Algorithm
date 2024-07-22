def solution(name, yearning, photo):
    answer = [0] * len(photo)

    name_yearning_dict = {n: y for n, y in zip(name, yearning)}

    for pp in range(len(photo)):
        for p in photo[pp]:
            if p in name_yearning_dict.keys():
                answer[pp] += name_yearning_dict[p]

    return answer
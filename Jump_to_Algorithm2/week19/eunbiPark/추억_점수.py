def solution(name, yearning, photo):

    miss = {n:y for n, y in zip(name, yearning)}
    result = [0] * len(photo)

    for i, p in enumerate(photo):
        for people in p:
            try : # if 문으로 변경 가능
                result[i] += miss[people]
            except:
                continue

    return result
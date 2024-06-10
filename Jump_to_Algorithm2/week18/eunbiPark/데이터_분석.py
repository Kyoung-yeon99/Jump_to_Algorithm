def solution(data, ext, val_ext, sort_by):
    index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    #     ret = list(filter(lambda x : x[index[ext]] < val_ext, data))
    #     ret.sort(key = lambda x: (x[index[sort_by]]))

    ret = sorted(filter(lambda x: x[index[ext]] < val_ext, data), key=lambda x: x[index[sort_by]])

    return ret
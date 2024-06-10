def solution(data, ext, val_ext, sort_by):
    answer = []
    text = ["code", "date", "maximum", "remain"]

    # ext 확인하여 ext_idx 지정, sort_by 확인하여 sort_idx 지정
    for i in range(4):
        if ext == text[i]:
            ext_idx = i
        if sort_by == text[i]:
            sort_idx = i

    # 조건 만족하는 데이터 append
    for i in range(len(data)):
        if data[i][ext_idx] < val_ext:
            answer.append(data[i])

    # 정렬하기
    answer.sort(key=lambda x: x[sort_idx])

    return answer
def solution(files):
    # 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현
    # 영문자로 시작해서 숫자 하나 이상 포함 - 100글자 이내, 영문대소문자, 숫자, 공백, 마침표, 빼기부호
    # HEAD는 한 글자 이상의 문자
    # NUMBER 최대 다섯 글자의 연속된 숫자 0 시작 가능 0-99999
    # TAIL 나머지 부분

    fs = []
    for idx, name in enumerate(files):
        h, head = 0, ''
        while not name[h].isdigit():  # head는 공백, 마침표, 빼기 부호 포함 -> lower() XXX
            if name[h].isalpha():
                head += name[h].lower()
            else:
                head += name[h]
            h += 1

        num = h
        while num < len(name) and name[num].isdigit():  # num < len(name) 조건이 없으면 Index Out of Range 에러 발생
            num += 1

        fs.append([idx, name, head, int(name[h:num])])

    fs.sort(key=lambda x: (x[2], x[3], x[0]))
    answer = [f[1] for f in fs]
    return answer

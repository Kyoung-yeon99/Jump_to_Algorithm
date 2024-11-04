# 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬
# head, number, tail 세 부분으로 구성됨

# 파일명을 쪼개야 함.
# head: 문자로 이뤄짐 (.isdigit() 함수로 체크?)
# number: 길이 5 이하, 0~99999
# tail: 나머지 부분(숫자 or 아무 글자 없을수도)

# 기준
# head: 대소문자 구분 x -> upper_case() 로 만들어서 정렬하기
# number: 숫자 기준으로 정렬하기  9< 10< 0011< 012 ... -> int()?
# tail: 만약 head, number의 숫자가 같을 경우, 원래 입력에 주어진 순서 유지


def solution(files):
    answer = []

    # 파일명 나눈 거 저장할 리스트
    sep = []

    for file in files:
        head = ''
        number = ''
        tail = ''

        # head 구분
        i = 0
        while i < len(file) and not file[i].isdigit():  # 숫자가 아닐때까지
            head += file[i]
            i += 1

        # number 추출
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1

        # tail 은 나머지
        tail += file[i:]  # 슬라이싱

        # 원래 이름 백업
        sep.append((head, number, tail, file))  # 몽땅 튜플로 저장

    # 3가지 기준에 맞춘 정렬 구현
    # head: 대문자로 바꾸기, number: 정수로 변환해 정렬, 원래 입력 순서유지
    sep.sort(key=lambda x: (x[0].upper(), int(x[1]), files.index(x[3])))

    for head, number, tail, original in sep:
        file_name = f"{head}{number}{tail}"
        # 정답에 추가
        answer.append(file_name)

    return answer
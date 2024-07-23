# 시간을 "HH:MM" 형식에서 분 단위로 변환하는 함수
def time2val(time):
    return int(time[:2]) * 60 + int(time[3:])  # 시간 부분을 분으로 변환하고 분 부분을 더함

def solution(book_time):
    dic = {}  # 각 분에 예약된 객실 수를 저장할 딕셔너리
    for book in book_time:
        st = time2val(book[0])  # 시작 시간을 분으로 변환
        en = time2val(book[1])  # 종료 시간을 분으로 변환
        for t in range(st, en + 10):  # 시작 시간부터 종료 시간 + 10분까지 반복
            if dic.get(t) is None:
                dic[t] = 1  # 해당 시간에 첫 예약이면 1로 초기화
            else:
                dic[t] += 1  # 이미 예약된 시간이면 예약 수를 1 증가

    return max(dic.values())  # 모든 시간대 중 최대 예약 수 반환
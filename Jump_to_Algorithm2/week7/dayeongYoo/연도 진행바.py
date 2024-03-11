# 해가 얼마나 지났는지 보여주는 진행률 바 만들기

# 월, 날짜, 연도, 시간, 분

month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 입력받는거 굉장히 까다롭.
# 특수문자 제거
input_str = input()
input_str = input_str.replace(',', '')
input_str = input_str.replace(':', ' ')

tmp = list(input_str.split())  # 다루기 쉽게 리스트화

month = tmp[0]
day = int(tmp[1])
year = int(tmp[2])
hour = int(tmp[3])
min = int(tmp[4])

# 연도-> 윤년 계산할 때 필요.
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    days[1] = 29  # 윤년은 29일까지.

# 달 별로 이전 달 날짜수 누적. # 이거를 어떻게 짜야 효율적일까. 그냥 if문으로? -> 너무 막노동
# 달의 이름을 인덱스로 가져와서 전체 12달에서 슬라이싱하기.
# 시간은?
total_time = sum(days) * 24 * 60  # 전체 시간 구하기.
mon_idx = month_name.index(month)
# 현재까지 흐른 시간 구하기
# TypeError: can only concatenate list (not "int") to list
# print(sum(days[:mon_idx + 1] + day)) # <-- 문제가 되는 부분. 연산자 앞은 리스트, 뒤는 숫자.
# print(sum(days[:mon_idx]) + day - 1)  # 1월 1일은 12월 31일 시간 + 현재 시간임.

cur_time = (sum(days[:mon_idx]) + day - 1) * 24 * 60 + hour * 60 + min
# 진행률
print(cur_time / total_time * 100)

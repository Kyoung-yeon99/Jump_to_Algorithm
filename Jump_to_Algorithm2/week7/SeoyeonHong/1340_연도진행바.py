
month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 
         'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

minutes_in_year = 365 * 24 * 60

M, d, y, t = input().split()
d, y, h, m = int(d[:-1]), int(y), int(t[:2]), int(t[3:])

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0): # 윤년일 경우 2월 하루 추가
    minutes_in_year += 24 * 60
    days_in_month[2] += 1

passed = sum(days_in_month[:month[M]]) * 24 * 60 + (d-1) * 24 * 60 + h * 60 + m
if passed != 0:
    print(passed / minutes_in_year * 100) 
else:
    print(0.0)


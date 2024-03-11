# Month DD, YYYY HH:MM
import sys
input = sys.stdin.readline


def check(year):  # 운년 확인
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


now = list(input().split())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0

if check(int(now[2])):  # 윤년이면
    days[1] = 29

idx = months.index(now[0])
for i in range(idx):
    cnt += days[i]
cnt += (int(now[1][:-1]) - 1)
cnt = cnt * 1440  # 24*60
hour = int(now[3][:2])*60
min = int(now[3][3:])
cnt = cnt + hour + min
print('%0.9f'%((cnt/(1440*sum(days)))*100))
# 절대/상대 오차는 10**(-9)까지 허용 -> 소수점 9번째자리까지 보여주기




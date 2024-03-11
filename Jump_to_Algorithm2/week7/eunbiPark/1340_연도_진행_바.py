month, d, y, t = input().split()
d = int(d[:-1])
y = int(y)
h, m = map(int, t.split(':'))
month_list = ["January" , "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if y%400 == 0 or (y % 4 == 0 and y % 100 != 0):
    day_list[1] += 1

total = sum(day_list) * 24 * 60

last_month_idx = month_list.index(month)
current_time = (sum(day_list[:last_month_idx]) + d - 1) * 24 * 60 + h * 60 + m

print(current_time / total * 100)
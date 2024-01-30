s = list(map(int, list(input())))

turn_zero = 0 # 0 -> 1
turn_one = 0 # 1 -> 0

for i in range(len(s) - 1):
    if s[i] == 0 and s[i + 1] == 1:
        turn_zero += 1
    elif s[i] == 1 and s[i + 1] == 0:
        turn_one += 1

if s[-1] == 0:
    turn_zero += 1
elif s[-1] == 1:
    turn_one += 1

print(min(turn_zero, turn_one))

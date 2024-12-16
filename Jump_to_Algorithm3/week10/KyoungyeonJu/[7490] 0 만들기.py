def make_zero(num, exp):
    if num == n:
        if eval(exp.replace(" ", "")) == 0:
            print(exp)
        else:
            return
    else:
        next_num = num + 1
        make_zero(next_num, exp + " " + str(next_num))
        make_zero(next_num, exp + "+" + str(next_num))
        make_zero(next_num, exp + "-" + str(next_num))


tc = int(input())
for _ in range(tc):
    n = int(input())
    make_zero(1, "1")
    print()

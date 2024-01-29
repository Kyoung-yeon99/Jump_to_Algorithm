num = int(input())


def check_vps(num):
    for i in range(num):
        bracket = input()
        vps_stack = []
        for j in bracket:
            if j == '(':
                vps_stack.append(j)
            elif j == ')' and '(' not in vps_stack:
                vps_stack.append(j)
            elif j == ')':
                vps_stack.pop()

        if len(vps_stack):
            print('NO')
        else:
            print('YES')


check_vps(num)

def recur(n):
    if n == 3:
        return ['***', '* *', '***']

    prev_star = recur(n // 3)

    result = []

    for star in prev_star:
        result.append(star * 3)

    for star in prev_star:
        result.append(star + ' ' * (n // 3) + star)

    for star in prev_star:
        result.append(star * 3)

    return result


n=int(input())
print('\n'.join(recur(n)))
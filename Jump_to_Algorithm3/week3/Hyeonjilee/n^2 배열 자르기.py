def solution(n, left, right):
    arr = []
    for id in range(left,right+1):
        r, c = id//n, id%n

        if c>=r+1:
            arr.append(c+1)
        else:
            arr.append(r+1)
    return arr

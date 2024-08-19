def solution(order):
    ans = 0
    stack = []
    n = len(order)
    idx, num = 0, 0
    
    while idx < n:
        # 번호를 찾을 때 까지 append
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx
        
    return idx

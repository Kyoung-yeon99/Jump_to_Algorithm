def solution(n, left, right):
    ans = []
    for i in range(left, right + 1):
        a = i//n
        b = i%n
        if a < b:
            a, b = b, a
        ans.append(a + 1)
    return ans 

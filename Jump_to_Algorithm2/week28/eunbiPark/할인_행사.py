from collections import Counter
def solution(want, number, discount):
    ans = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    for i in range(len(discount) - 9):
        c = Counter(discount[i: i + 10])
        if c == check:
            ans += 1
    
    return ans
